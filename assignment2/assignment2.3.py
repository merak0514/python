# 2.3 
# Write a program to ask for hours and rate per hour to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (96.25).
# Use input to read a string and float() to convert the string to a number.
# Do not worry about error checking or bad user data.
#
# This first line is provided for you.

hrs = input("Enter Hours:")
rate = input("Enter Rate Per Hour:")
hrs = float(hrs)
rate = float(rate)
pay = hrs * rate
print("Pay:", pay)
