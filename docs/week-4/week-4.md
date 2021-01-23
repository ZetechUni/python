# Week 4: Into Data

# Anaconda

[Anaconda](https://www.anaconda.com/) is an open source distribution of Python and R for data science. It includes more than 1500 packages, a graphical interface called Anaconda Navigator, a command line interface called Anaconda prompt and a tool called Conda.

## Conda

Python code often relies on external libraries stored in packages. Conda is an open source package management system and environment management system. Conda helps you manage environments and install packages for Jupyter Notebooks.

## Documentation

- [Conda home page](https://docs.conda.io/)
- [Managing Conda environments](https://docs.conda.io/projects/conda/latest/user-guide/tasks/manage-environments.html) to find links and instructions for creating Conda environments, activating, and de-activating Conda environments 
- [Managing packages](https://docs.conda.io/projects/conda/latest/user-guide/getting-started.html#managing-packages) to learn how to install packages in a Conda environment
- [Conda cheat sheet](https://docs.conda.io/projects/conda/latest/user-guide/cheatsheet.html) is a handy quick reference of common Conda commands

# CSV Files and Jupyter Notebooks

CSV files are comma separated variable file. CSV files are frequently used to store data. In order to access the data in a CSV file from a Jupyter Notebook you must upload the file. 

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)

# pandas

[pandas](https://pandas/pydata.org​) is an open source Python library contains a number of high performance data structures and tools for data analysis.

## Documentation

- [Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) stores one dimensional arrays
- [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html) stores two dimensional arrays and can contain different datatypes

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)

# Jupyter Notebooks

Jupyter Notebooks are an open source web application that allows you to create and share Python code. They are frequently used for data science. The code samples in this course are completed using Jupyter Notebooks which have a .ipynb file extension.

## Documentation

- [Jupyter](https://jupyter.org/) to install Jupyter so you can run Jupyter Notebooks locally on your computer
- [Jupyter Notebook viewer](https://nbviewer.jupyter.org/) to view Jupyter Notebooks in this GitHub repository without installing Jupyter
- [Azure Notebooks](https://notebooks.azure.com/) to create a free Azure Notebooks account to run Notebooks in the cloud
- [Create and run a notebook](https://docs.microsoft.com/azure/notebooks/tutorial-create-run-jupyter-notebook?WT.mc_id=python-c9-niner) is a tutorial that walks you through the process of using Azure Notebooks to create a complete Jupyter Notebook that demonstrates linear regression
- [How to create and clone projects](https://docs.microsoft.com/azure/notebooks/create-clone-jupyter-notebooks?WT.mc_id=python-c9-niner) to create a project
- [Manage and configure projects in Azure Notebooks](https://docs.microsoft.com/azure/notebooks/configure-manage-azure-notebooks-projects?WT.mc_id=python-c9-niner) to upload Notebooks to your project

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)

# Examining pandas DataFrame contents

The pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) is a structure for storing two-dimensional tabular data.

## Common functions

- [head](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) returns the first *n* rows from the DataFrame
- [tail](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html) returns the last *n* rows from the DataFrame
- [shape](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html) returns the dimensions of the DataFrame (e.g. number of rows and columns)
- [info](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html) provides a summary of the DataFrame content including column names, their datatypes, and number of rows containing non-null values

# Query a pandas DataFrame

The pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)  is a structure for storing two-dimensional tabular data.

## Common properties

- [loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) returns specific rows and columns by specifying column names
- [iloc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html) returns specific rows and columns by specifying column positions

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)

# Read and write CSV files from pandas DataFrames

You can populate a DataFrame with the data in a CSV file.

## Common functions and properties

- [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) reads a comma-separated values file into a DataFrame
- [to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) writes contents of a DataFrame to a comma-separated values file
- [NaN](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html) is the default representation of missing values

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)
