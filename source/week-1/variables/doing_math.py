# Because the variables are assigned numeric values when created
# Python knows they are numeric variables
first_num = 6
second_num = 2

# FIRST WAY OF DOING IT
"""# You can perform a variety of math operations on numeric values
print('addition')
print(first_num + second_num)
print('subtraction')
print(first_num - second_num)
print('multiplication')
print(first_num * second_num)
print('division')
print(first_num / second_num)
print ('exponent')
print(first_num ** second_num)
"""

# SECOND WAY OF DOING IT

# importing operator module
import operator

# using add() to add two numbers
print("The addition of numbers is :", end="")
print(operator.add(first_num, second_num))

# using sub() to subtract two numbers
print("The difference of numbers is :", end="")
print(operator.sub(first_num, second_num))

# using mul() to multiply two numbers
print("The multiplication of numbers is :", end="")
print(operator.mul(first_num, second_num))

# using truediv() to divide two numbers
print("The division of numbers is :", end="")
print(operator.truediv(first_num, second_num))

# using pow() to find the power of two numbers
print("The power of numbers is :", end="")
print(operator.pow(first_num, second_num))
