# Home Price Calculator Version 0.031

# Import pandas, numpy, matplotlib, and sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Importing the data from a network request
scan = pd.read_csv('https://raw.githubusercontent.com/bursteinalan/Data-Sets/master/Housing/House%20Prediction%20Data.csv')

# Build a linear regression class
class analyze_values:
  def __init__(self, prediction_data):
    # Prediction_data is the raw house data from the csv file
    self.prediction_data = prediction_data
  def set_independent_variables(self,independent_variables):
    # Dataset of independent variables to be analyzed
    self.independent_variables = independent_variables
  def print_independent_variables(self):
    print(self.independent_variables)
  def do_regression(self):
    # Add SalePrice column to dataset of independent variables
    independent_dependent_variables=self.independent_variables.copy()
    independent_dependent_variables.append('SalePrice')


    # Copy columns I will use into a new dataframe
    self.df = scan[independent_dependent_variables].copy()

    # Eliminate columns with blank values
    self.modifieddf = self.df.dropna()
    self.df_X_train = self.modifieddf[self.independent_variables][:-20]
    self.df_X_test = self.modifieddf[self.independent_variables][-20:]

    # Split the targets into training/testing sets
    self.df_Y_train = self.modifieddf[['SalePrice']][:-20]
    self.df_Y_test = self.modifieddf[['SalePrice']][-20:]

    # Create linear regression object
    self.reg = linear_model.LinearRegression()

    # Train the model using the training sets
    self.reg.fit(self.df_X_train, self.df_Y_train)

    # Make predictions using the model
    self.eSalePrice = self.reg.predict(self.df_X_test)

  def print_report(self):
    print("Independent variables: \n",self.independent_variables)

    # Format predicted prices
    eSalePriceFormatted = [0] * len(self.eSalePrice)
    for n in range(len(self.eSalePrice)):
      eSalePriceFormatted[n] = "${:,.2f}".format(float(self.eSalePrice[n]))

    # Show the key statistics to evaluate the model
    df_output = self.df_X_test.copy()
    df_output["Predicted Price"] = eSalePriceFormatted
    print("Predicted prices for tested square footage and number of bedrooms: \n", df_output)
    print("Coefficients: \n", self.reg.coef_)
    print("Intercept: \n", self.reg.intercept_)

    # R^2: the proportion of the variance that's explained by the model
    print("R^2-value: %.2f" % self.reg.score(self.df_X_test,self.df_Y_test))

# Compare different combinations of independent variables
myAV = analyze_values(scan)
myAV.set_independent_variables(['GrLivArea','BedroomAbvGr'])
myAV.do_regression()
myAV.print_report()

myAV.set_independent_variables(['GrLivArea','BedroomAbvGr', 'YearBuilt'])
myAV.do_regression()
myAV.print_report()

myAV.set_independent_variables(['GrLivArea','BedroomAbvGr', 'YearBuilt', 'FullBath'])
myAV.do_regression()
myAV.print_report()

myAV.set_independent_variables(['GrLivArea','BedroomAbvGr', 'YearBuilt', 'GarageCars'])
myAV.do_regression()
myAV.print_report()

myAV.set_independent_variables(['GrLivArea','BedroomAbvGr', 'GarageCars'])
myAV.do_regression()
myAV.print_report()

