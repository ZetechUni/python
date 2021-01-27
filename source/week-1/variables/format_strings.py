# FIRST WAY
# the capitalize function will return the string with 
# the first letter uppercase and the rest of the word lowercase

# Ask the user for their first and last name // it does not matter how the user types it:
# ALEX, alex, aLEX etc. --> it will be saved in the memory as Alex (Fist letter will be with uppercase)
first_name = input('What is your first name? ').capitalize()
last_name = input('What is your last name? ').capitalize()

print('Hello ' + first_name + ' ' + last_name)


# SECOND WAY
# Ask the user for their first and last name
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# the capitalize function will return the string with 
# the first letter uppercase and the rest of the word lowercase
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

