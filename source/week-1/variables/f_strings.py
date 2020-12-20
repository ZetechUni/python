# Only available for python 3.6+
# This new way of formatting strings lets you 
# use embedded Python expressions inside string constants.

name = input("What is your name? ")
subject = input("What subject do you like? ")
print(f"{name}'s favorite subject is {subject}.")

a = 5
b = 10
sum = a + b
print(f'{a} plus {b} is equal to {sum}.')
