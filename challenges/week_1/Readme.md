# Bus Fare Challenge - Week 1

## Challenge

Write a program that does the following:

1. gets today's date and stores it in a variable `'date'`
2. uses today's date to get the name on the day of the week written in short form with the first letter capitalized eg. `'Fri'` if today were Friday and assigns it a variable `'day'`
3. uses if statements to determine the today's fare following these bus fare schedule:

   - monday - friday --> 100
   - saturday --> 60
   - sunday --> 80
4. Prints the results in this format  
    >Date:    2021-01-05  
    >Day:     Tue  
    >Fare:    100  

## Evaluation

Run the [Checker](checker.py) file to evaluate your code. If all tests pass, your code will be the correct solution. If any fail, check the error messages and make changes to your code and repeat.

## Note

1. Your solution must be written in the [bus_fare_challenge](bus_fare_challenge.py) file and its name should never be changed.  
2. Your program must make use of the following variable names:
   - `'date'`
   - `'day'`
   - `'fare'`  
*Failure to which all your tests will fail.*  
3. The **Checker** file should **never** be **altered** at any cost.


Pseudo-code for the project

Step 1: obtain the date today using the datetime module
step 2: obtain the day in the form of "Mon", "Tue" etc
step 3: make a list of busfares with an accompanying day 
step 4: check if the day today is in the list of bus fares and then print the dates and fare.
