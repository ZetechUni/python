# Python BootCamp

![python-logo](python.svg)

<div align='center'>
    Facebook Developers Circle Nairobi at Zetech University || CodeIT, Zetech University
</div>

## 5 Weeks Of Python (Roadmap)

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
