# 5.2
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number, catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

big_number = None
small_number = None
while True:
    number = input(
        "input a integer please, if you don't want to continue, type done ")
    if number == 'done':
        break
    try:
        number = int(number)
    except:
        print('Invalid input')
        continue
    if big_number == None:
        big_number = number
        small_number = number
    else:
        if number > big_number:
            big_number = number
        if number < small_number:
            small_number = number
print('Maximum is', big_number)
print('Minimum is', small_number)
