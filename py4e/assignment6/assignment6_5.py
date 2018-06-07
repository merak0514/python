# 6.5
# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
# X-DSPAM-Confidence:    0.8475

text = "X-DSPAM-Confidence:    0.8475"
space = text.find(':')
number = text[space + 1:]
try:
    number = float(number)
except:
    print('Fxxxxxxxxxxk')
print(number)
