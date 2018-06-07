# 5.1
# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
numbers_inputed = 0
sum = 0.0
while True:
    number = input('number: ')
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print('Invalid input')
        continue
    numbers_inputed = numbers_inputed + 1
    sum = sum + number
average = sum / numbers_inputed
print(sum, numbers_inputed, average)
