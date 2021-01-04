# Splitting test and training data with scikit-learn

[scikit-learn](https://scikit-learn.org/) is a library of tools for predictive data analysis, which will allow you to prepare your data for machine learning and create models.

## Common functions

- [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) splits arrays into random train and test subsets
  - Main Parameters
    - `X` - Dataframe containing only the features you want to use for **training**
    - `y` - Dataframe containing only the features you want to **predict**
    - `test_size` - If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split.
  - Returns
    - `X_train` - Includes your the independent variables,these will be used to train the model. If we have specify the `test_size = 0.4` for instance, this means 60% of observations from your complete data will be used to train/fit the model and rest 40% will be used to test the model.
    - `X_test` - This is remaining 40% portion of the independent variables from the data which will not be used in the training phase and will be used to make predictions to test the accuracy of the model.
    - `y_train` - This is your dependent variable which needs to be predicted by this model, this includes category labels against your independent variables, we need to specify our dependent variable while training/fitting the model.
    - `y_test` - This data has category labels for your test data, these labels will be used to test the accuracy between actual and predicted categories.

## Microsoft Learn Resources

Explore related tutorials on [Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner).

- [Intro to machine learning with Python and Azure Notebooks](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)
