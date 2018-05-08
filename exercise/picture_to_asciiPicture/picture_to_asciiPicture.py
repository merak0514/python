# 灰度公式：gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

from PIL import Image
import argparse
import re

WIDTH = 60
HEIGHT = 25
picture_name = ''

paser = argparse.ArgumentParser(prog="pic2ascii")
# paser.add_argument('file')
#
#
# args = paser.parse_args()
# print(args.file)

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_picture():
    global picture_name
    picture_name = input('Picture name: ')
    try:
        im = Image.open(picture_name)
    except:
        print('No such file')
        quit()
    im = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    return im


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    step = 257/len(ascii_char)
    chosen_char = ascii_char[int(gray/step)]
    return chosen_char
# print(get_char(256,256,256))


if __name__ == '__main__':
    im = get_picture()
    txt = '/*\n'
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += 'x\n'
    txt += '*/\n'
    picture_name = re.findall('(\w+)\.', picture_name)[0]

    fhand = open(picture_name + '.cpp', 'wb')
    fhand.write(txt.encode())
