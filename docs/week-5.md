# Week 5

# Visualizing data with Matplotlib

[Matplotlib](https://matplotlib.org/) gives you the ability to draw charts which can be used to visualize data.

## Common tools and functions

- [pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#module-matplotlib.pyplot) provides the ability to draw plots similar to the MATLAB tool
- [pyplot.plot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) plots a graph
- [pyplot.show](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show) displays figures such as a graph
- [pyplot.scatter](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html?highlight=scatter%20plot#matplotlib.pyplot.scatter) is used to draw scatter plots, a diagram that shows the relationship between two sets of data

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)


# Handling duplicates and rows with missing values

When preparing data for machine learning you need to remove duplicate rows and you may need to delete rows with missing values.

## Common functions

- [dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) removes rows with missing values
- [duplicated](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) returns a True or False to indicate if a row is a duplicate of a previous row
- [drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) returns a DataFrame with duplicate rows removed

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)

# Testing a model

Once a model is built it can be used to predict values. You can provide new values to see where it would fall on the spectrum, and test the generated model.

## Common classes and functions

- [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) fits a linear model
- [LinearRegression.predict](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html?highlight=linearregression#sklearn.linear_model.LinearRegression.predict) is used to predict outcomes for new data based on the trained linear model

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)

# NumPy vs pandas

There are numerous libraries available for use for data scientists. NumPy and pandas are two of the most common.

Some operations may return different data types. You can use the Python function [type](https://docs.python.org/3/library/functions.html#type) to determine the type of an object.

## NumPy

[NumPy](https://numpy.org/) is a Python package for scientific computing that includes a array and dictionary type objects for data analysis.

### Common object

- [array](https://numpy.org/doc/1.18/reference/generated/numpy.array.html?highlight=array#numpy.array) creates an N-dimensional array object

## pandas

[pandas](https://pandas.pydata.org/) is a Python package for data analysis that includes a 1 dimensional and 2 dimensional array objects

### Common objects

- [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) stores a one dimensional array
- [DataFrame](https://pandas.pydata.org/docs/reference/frame.html) stores a two-dimensional array

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)

# Removing and splitting DataFrame columns

When preparing data for machine learning you may need to remove specific columns from the DataFrame.

## Common functions

- [drop](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html) deletes specified columns from a DataFrame

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)

# Splitting test and training data with scikit-learn

[scikit-learn](https://scikit-learn.org/) is a library of tools for predictive data analysis, which will allow you to prepare your data for machine learning and create models.

## Common functions

- [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) splits arrays into random train and test subsets

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)


# Train a linear regression model with scikit-learn

[Linear regression](https://en.wikipedia.org/wiki/Linear_regression) is a common algorithm for predicting values based on a given dataset.

## Common classes and functions

- [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) fits a linear model
- [LinearRegression.fit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html?highlight=linearregression#sklearn.linear_model.LinearRegression.fit) is used to fit the linear model based on training data

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)
