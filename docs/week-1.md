# Week 1: Environment Setup and Introduction

### Downloading Python
Python comes pre-installed on Linux OS. For Windows you will have to Download.
Download Python [here](https://www.python.org/downloads/)

### Resources
[Python For Beginnes](https://docs.microsoft.com/en-us/windows/python/beginners)

### Text Editors

Use a text-editor of your choice:

Recommended are:

[Visual Studio Code](https://code.visualstudio.com/)
[Atom](https://atom.io/)
[Sublime Text](https://www.sublimetext.com/)

### Git and GitHub Setup.

Note that you have to pass the challenges in git and github to proceed to the next stages.
They are essential tools in development for code sharing and collaboration.

[Get Started Here](git-github-setup.md)

[Raise an Issue if encountering a blocker](https://github.com/ZetechUni/python-bootcamp/issues/new)

## Practice Code

1. [Print](../source/week-1/print)
2. [Variables](../source/week-1/variables)
3. [Dates](../source/week-1/dates)
4. [Error Handling](../source/week-1/error-handling)
5. [Conditions](../source/week-1/conditions)


<!-- code documentations -->


1. ## Print

   The print function allows you to send output to the terminal

   - [print](https://docs.python.org/3/library/functions.html#print)

   Strings can be enclosed in single quotes or double quotes

   - "this is a string"
   - 'this is also a string'

   The input function allows you to prompt a user for a value

   - [input](https://docs.python.org/3/library/functions.html#input)

   Parameters:

   - `prompt`: Message to display to the user

   return value:

   - string value containing value entered by user

2. ## Variables: Numeric

   Python can store and manipulate numbers. Python has two types of numeric values: integers (whole numbers) or float (numbers with decimal places)

   - [numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

   When naming variables follow the PEP-8 Style Guide for Python Code

   - [PEP-8 Style Guide](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

   Converting to numeric values

   - [int](https://docs.python.org/3/library/functions.html#int)
   - [float](https://docs.python.org/3/library/functions.html#float)

3. ## Variables: String

   Python can store and manipulate strings. Strings can be enclosed in single or double quotes. There are a number of string methods you can use to manipulate and work with strings

   - [strings](https://docs.python.org/3/tutorial/introduction.html#strings)
   - [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

   Converting to string values

   - [str](https://docs.python.org/3/library/functions.html#func-str)

   When naming variables follow the PEP-8 Style Guide for Python Code

   - [PEP-8 Style Guide](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

4. ## Dates

   The [datetime module](https://docs.python.org/3/library/datetime.html) contains a number of classes for manipulating dates and times.

   Date and time types:

   - `date` stores year, month, and day
   - `time` stores hour, minute, and second
   - `datetime` stores year, month, day, hour, minute, and second
   - `timedelta` a duration of time between two dates, times, or datetimes

   When naming variables follow the PEP-8 Style Guide for Python Code

   - [PEP-8 Style Guide](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

   Converting from string to datetime

   - [strptime](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)

5. ## Error Handling

   Error handling in Python is managed through the use of [try/except/finally](https://docs.python.org/3.7/reference/compound_stmts.html#except)

   Python has numerous [built-in exceptions](https://docs.python.org/3.7/library/exceptions.html). When creating `except` blocks, they need to be created from most specific to most generic according to the [hierarchy](https://docs.python.org/3.7/library/exceptions.html#exception-hierarchy).

6. ## Conditions

   Conditional execution can be completed using the [if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) statement

   `if` syntax

   ```python
   if expression:
      # code to execute
   else:
      # code to execute
   ```

   [Comparison operators](https://docs.python.org/3/library/stdtypes.html#comparisons)

   - < less than
   - < greater than
   - == is equal to
   - \>= greater than or equal to
   - <= less than or equal to
   - != not equal to

7. ## Multiple Conditions

   Conditional execution can be completed using the [if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) statement. Adding `elif` allows you to check multiple conditions

   `if` syntax

   ```python
   if expression:
      # code to execute
   elif expression:
      # code to execute
   else:
      # code to execute
   ```

   [Boolean operators](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

   - **x _or_ y** - If either x OR y is true, the expression is executed

   [Comparison operators](https://docs.python.org/3/library/stdtypes.html#comparisons)

   - < less than
   - < greater than
   - == is equal to
   - \>= greater than or equal to
   - <= less than or equal to
   - != not equal to
   - **x _in_ [a,b,c]** Does x match the value of a, b, or c
