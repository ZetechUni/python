# Python BootCamp

![python-logo](python.svg)

<div align='center'>
    Facebook Developers Circle Nairobi at Zetech University || CodeIT, Zetech University
</div>

## 5 Weeks Of Python (Roadmap)


## Week 1: Environment Setup and Introduction

### Downloading Python
Python comes pre-installed on Linux OS. For Windows you will have to Download.
Download Python [here](https://www.python.org/downloads/)

### Resources

[Setting Up](https://docs.microsoft.com/en-us/windows/python/beginners)

<details>
<summary>Week 1</summary>

1. Print
2. Variables: Numeric
3. Variables: String
4. Dates
5. Error Handling
6. Conditions
7. Multiple Conditions

</details>

<details>
<summary>Week 2</summary>

1. Collections (list, arrays, ranges)
2. Loops
3. Functions
4. Functions with Parameters
5. Modules & Packages
6. JSON with Python
7. Decorators

</details>

<details>
<summary>Week 3</summary>

1. Formatting & Linting
2. Lambdas
3. Classes
4. Inheritance
5. Mixins
6. File System Management
7. Asynchronous Programming

</details>

<details>
<summary>Week 4: Data Tools</summary>

1. Jupyter Notebooks
2. Anaconda, Conda & Colabs
3. Introduction to Pandas
4. Pandas: dataframe contents
5. Pandas: dataframe querry
6. CSV files & Jupyter
7. Read/Write CSV Files with Pandas

</details>

<details>
<summary>Week 5: Data Tools</summary>

1. Removing & Splitting dataframe columns
2. Duplicate rows & Missing Values
3. Split Testing & Data Training with scikit learn
4. Train linear Regression Model with scikit learn
5. Model testing
6. Numpy & Pandas
7. Visualizing data with Matplotlib

</details>

## Setting Up Your Developer Environment

### Python

> Preferably version 3,

[Download Python](https://www.python.org/downloads/)

### git

[Download Git](https://git-scm.com/)

[Git Configuration](https://dev.to/chrisachinga/git-and-github-install-configure-51pa)

### GitHub Account

[Create Account](https://github.com)

## What You Need:

As the Bootcamp is open to anyone, we encourage members of our community, Facebook Developers Circle Nairobi at Zetech University to actively engange in the activities.

## Contributing To The Repo

1. Fork the repo to your GitHub Account. [Guide](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)
2. Create a new branch with a name in conjuction to your update/fix

   [Read More On Contributions](CONTRIBUTING.md)

<details>

<summary># WEEK 1: Introduction </summary>

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

</details>

<details>
<summary># Week 2: The Basics</summary>

1. ## Collections (list, arrays, ranges)

   Collections are groups of items. Python supports several types of collections. Three of the most common are dictionaries, lists and arrays.

   ### Lists

   [Lists](https://docs.python.org/3/tutorial/introduction.html#lists) are a collection of items. Lists can be expanded or contracted as needed, and can contain any data type. Lists are most commonly used to store a single column collection of information, however it is possible to [nest lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)

   ### Arrays

   [Arrays](https://docs.python.org/3/library/array.html) are similar to lists, however are designed to store a uniform basic data type, such as integers or floating point numbers.

   ### Dictionaries

   [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) are key/value pairs of a collection of items. Unlike a list where items can only be accessed by their index or value, dictionaries use keys to identify each item.

2. ## Loops

   ### For loops

   [For loops](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) takes each item in an array or collection in order, and assigns it to the variable you define.

   ```python
   names = ['Christopher', 'Susan']
   for name in names:
      print(name)
   ```

   ### While loops

   [While loops](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) perform an operation as long as a condition is true.

   ```python
   names = ['Christopher', 'Susan']
   index = 0
   while index < len(names):
      name = names[index]
      print(name)
      index = index + 1
   ```

3. ## Functions

   Functions allow you to take code that is repeated and move it to a module that can be called when needed. Functions are defined with the `def` keyword and must be declared before the function is called in your code. Functions can accept parameters and return values.

   - [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

   ```python
   def functionname(parameter):
      # code to execute
      return value
   ```

4. ## Functions with Parameters

   Functions allow you to take code that is repeated and move it to a module that can be called when needed. Functions are defined with the `def` keyword and must be declared before the function is called in your code. Functions can accept one or more parameters and return values.

   - [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

   ```python
   def function_name(parameter):
      # code to execute
      return value
   ```

   Parameters can be assigned a [default value](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) making them optional when the function is called.

   ```python
   def function_name(parameter=default):
      # code to execute
      return value
   ```

   When you call a function you may specify the values for the parameters using positional or [named notation](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)

   ```python
   def function_name(parameter1, parameter2):
      # code to execute
      return value

   # Positional notation pass in arguments in same order as parameters are declared
   result = function_name(value1,value2)

   # Named notation
   result = function_name(parameter1=value1, parameter2=value2)
   ```

5. ## Modules & Packages

   ### Modules

   [Modules](https://docs.python.org/3/tutorial/modules.html) allow you to store reusable blocks of code, such as functions, in separate files. They're referenced by using the `import` statement.

   ```python
   # import module as namespace
   import helpers
   helpers.display('Not a warning')

   # import all into current namespace
   from helpers import *
   display('Not a warning')

   # import specific items into current namespace
   from helpers import display
   display('Not a warning')
   ```

   ### Packages

   [Distribution packages](https://packaging.python.org/glossary/#term-distribution-package) are external archive files which contain resources such as classes and functions. Most every application you create will make use of one or more packages. Imports from packages follow the same syntax as modules you've created. The [Python Package index](https://pypi.org/) contains a full list of packages you can install using [pip](https://pip.pypa.io/en/stable/).

   ### Virtual environments

   [Virtual environments](https://docs.python.org/3.7/tutorial/venv.html) allow you to install packages into an isolated folder. This allows you to better manage versions.

   ```console

   ```

6. ## JSON with Python

   Many APIs return data in [JSON](https://json.org/), JavaScript Object Notation. JSON is a standard format that can is readable by humans and parsed or generated by code.

   JSON is built on two structures:

   - collections of key/value pairs
   - lists of values

   JSON Linters will format JSON so it easier to read by a human. The following website have JSON linters:

   - [JSONLint](https://jsonlint.com/)
   - [ConvertJson.com](http://www.convertjson.com/jsonlint.htm)
   - [JSON schema linter](https://www.json-schema-linter.com/)

   Python includes a [json](https://docs.python.org/2/library/json.html) module which helps you encode and decode JSON

7. ## Decorators

   [Decorators](https://www.python.org/dev/peps/pep-0318/) are similar to attributes in that they add meaning or functionality to blocks of code in Python. They're frequently used in frameworks such as [Flask](http://flask.pocoo.org/) or [Django](https://www.djangoproject.com/). The most common interaction you'll have with decorators as a Python developer is through using them rather than creating them.

   ```python
   # Example decorator
   @log(True)
   def sample_function():
      print('this is a sample function')
   ```

</details>
