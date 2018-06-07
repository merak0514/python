# 4.6
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of time-and-a-half in a function called computepay(),
# and use the function to do the computation.
# The function should return a value.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.


def computepay(time, rate):
    if (time <= 0) | (rate <= 0):
        print('Please input a time>0 and a rate>0')
    elif time <= 40:
        pay = time * rate
    else:
        pay = 40 * rate + 1.5 * rate * (time - 40)
    return pay


try:
    time = float(input('time'))
    rate = float(input('rate'))
except:
    print('Please input a number')
    quit()
pay = computepay(time, rate)
print(pay)
