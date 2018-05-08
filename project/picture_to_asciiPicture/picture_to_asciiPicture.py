# 灰度公式：gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

from PIL import Image
import argparse
import re


picture_name = ''

paser = argparse.ArgumentParser(prog="pic2ascii")
# paser.add_argument('file')
#
#
# args = paser.parse_args()
# print(args.file)

ascii_char1 = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ascii_char2 = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxr                            . ")


def get_picture():
    global picture_name, width, height

    picture_name = input('Picture name: ')
    try:
        im = Image.open(picture_name)
    except:
        print('No such file')
        quit()
    print(im.size)
    width = im.size[0]
    height = im.size[1]
    while width > 80 or height > 80:
        width = int(width / 2)
        height = int(height / 2)
    im = im.resize((width, height), Image.ANTIALIAS)
    return im


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    step = 257/len(ascii_char1)
    chosen_char = ascii_char1[int(gray / step)]
    return chosen_char
# print(get_char(256,256,256))


if __name__ == '__main__':
    im = get_picture()
    txt = '/*\n'
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))
        txt += 'x\n'
    txt += '*/\n'
    picture_name = re.findall('(\w+)\.', picture_name)[0]

    fhand = open(picture_name + '.cpp', 'wb')
    fhand.write(txt.encode())
    print("Done!")
