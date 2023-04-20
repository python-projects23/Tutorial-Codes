###############################
# Python Quickies #Tip 001
# HOW TO USE WALRUS OPERATOR IN PYTHON 3.8 & ABOVE
###############################
"""
The := Operator can be used to assign a
variable inline. It can simplify your code
"""

# Before Python 3.8
# text = input('Enter something ')
# if text is not None:
#     print(text)

# Using Walrus operator
while text := input('Enter something '):
    print(text)

