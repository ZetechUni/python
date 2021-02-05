"""
Pseudo code for the challenge
1. create a converter function
2. Obtain the name of the user using the input function
3. print the name of the user with the choices to choose from
4. within the converter function specify the individual converter functions.
5.  from the choice selected by user, run the corresponding converter function
6. Return the results to the user.
"""

def converter():
    # ask the name input from the user
    name = str(input("Input your name:"))
    # print the name of the user and the hello message
    print("Hello {}, welcome to your personal converter.".format(name))
    print("Please choose which conversion you would like to perform:")
    print("1 - convert cm to inches\n2 - convert percent to letter grade\n3 - convert cups to ml\n4 - convert grams to ounces\n5 - convert fahrenheit to celsius\n")
    # ask the user to choose the number for the choice
    choice = int(input("Choice:"))

    # the function converting cm to inches
    def cm_to_inch():
        num = int(input("Value in cm to convert: "))
        result = "{}cm = {}inches".format(num, num*0.39370)
        print(result)
    # function getting the percent and giving the respective letter grade

    def percent_to_letter_grade():
        num = float(input("Percent to convert to letter grade: "))
        num1 = int(num)
        if num1 in range(80, 101, 1):
            result = "A"
        if num1 in range(70, 80, 1):
            result = "B"
        if num1 in range(60, 70, 1):
            result = "C"
        if num1 in range(50, 60, 1):
            result = "D"
        if num1 in range(40, 50, 1):
            result = "E"
        if num1 in range(30, 40, 1):
            result = "F"
        result = "{}% = {}".format(num, result)
        print(result)

    # function changing cups to ml
    def cups_to_ml():
        num = int(input("Enter the number of cups to convert: "))
        result = "{} cups = {} ml".format(num, num*250)
        print(result)

    # functin changing grams to ounces
    def grams_to_ounces():
        num = float(
            input("Enter the number of grams to convert to ounces: "))
        result = "{} grams = {} ounces".format(num, num*0.0352)
        print(result)

    # function changing farenheit to celcius
    def farenheit_to_celcius():
        num = float(input("Value to convert Farenheit to Celcius: "))
        result = "{} Farenheit = {}\u00b0 C".format(
            num, round((num-32)*5/9), 2)
        print(result)
    if choice == 1:
        cm_to_inch()
    elif choice == 2:
        percent_to_letter_grade()
    elif choice == 3:
        cups_to_ml()
    elif choice == 4:
        grams_to_ounces()
    elif choice == 5:
        farenheit_to_celcius()
    else:
        print("The choice is not valid.")
    return "Goodbye {}".format(name)


if __name__ == "__main__":
    converter()
