# In Python, there are several ways to print multiple variables. Here are some examples:

# Using the print() function and separating variables with commas:
x = 10
y = 20
print(x, y)  # Output: 10 20


# Using formatted string literals (f-strings):
x = 10
y = 20
print(f"x={x}, y={y}")  # Output: x=10, y=20


# Using the str.format() method:
x = 10
y = 20
print("x={}, y={}".format(x, y))  # Output: x=10, y=20


# Using %-formatting:
x = 10
y = 20
print("x=%s, y=%s" % (x, y))  # Output: x=10, y=20


# Concatenating variables as strings:
x = 10
y = 20
print(str(x) + " " + str(y))  # Output: 10 20
