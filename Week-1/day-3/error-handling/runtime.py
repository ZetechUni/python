# Error Handling
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
finally:
    print('This always runs on success or failure')

# Use while to create an infinite loop that will run
# # until false is returned (correct input in this case)
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# Instead of letting python to shout at the user "ValueError"
# we catch the anticipated error and display a polite message