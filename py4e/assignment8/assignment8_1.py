# 8.1
# Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.


def chop(a):
    del a[len(a) - 1]
    del a[0]
    return None


def middle(a):
    return(a[1:len(a) - 1])
