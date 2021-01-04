# CSV Files and Jupyter Notebooks

The so-called **CSV** (Comma Separated Values) format is the most common import and export format for spreadsheets and databases. The CSV format was used for many years prior to attempts to describe the format in a standardized way.

Python has an in-built csv module which implements classes to read and write tabular data in CSV format.

```python
# format example
>>> import csv
>>> with open('./airports.csv') as file:
...     data = csv.reader(file)
...     for row in data:
...     print(*row) # * is used to unpack lists
Name City Country
Seattle-Tacoma Seattle USA
Dulles Washington USA
Heathrow London United Kingdom
Schiphol Amsterdam Netherlands
Changi Singapore Singapore
Pearson Toronto Canada
Narita Tokyo Japan
```

A this module has a lot more features, checkout [more details](https://docs.python.org/3/library/csv.html).

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)
