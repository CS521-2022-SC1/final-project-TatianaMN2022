# Home Price Calculator Version 0.021

# Import pandas, numpy, matplotlib, and sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Importing the data from a network request
scan = pd.read_csv('https://raw.githubusercontent.com/bursteinalan/Data-Sets/master/Housing/House%20Prediction%20Data.csv')

# Copy columns I will use into a new dataframe
df = scan[['GrLivArea','BedroomAbvGr','SalePrice']].copy()

# Eliminate rows with blank values
modifieddf = df.dropna()

# Split the data into training/testing sets
df_X_train = modifieddf[['GrLivArea','BedroomAbvGr']][:-20]
df_X_test = modifieddf[['GrLivArea','BedroomAbvGr']][-20:]

df_Y_train = modifieddf[['SalePrice']][:-20]
df_Y_test = modifieddf[['SalePrice']][-20:]

# Create linear regression object
reg = linear_model.LinearRegression()

# Train the model using the training sets
reg.fit(df_X_train, df_Y_train)


# Define the output of the regression model (y-bar)
eSalePrice=reg.predict(df_X_test)

# Format predicted prices
eSalePriceFormatted = [0] * len(eSalePrice)
for n in range(len(eSalePrice)):
    eSalePriceFormatted[n] = "${:,.2f}".format(float(eSalePrice[n]))


# Show the key statistics to evaluate the model
df_output = df_X_test.copy()
df_output["Predicted Price"] = eSalePriceFormatted
print("Predicted prices for tested square footage and number of bedrooms: \n",df_output)
print("Coefficients: \n", reg.coef_)
print("Intercepter: \n", reg.intercept_)

# R^2: the proportion of the variance that's explained by the model
print("R^2-value: %.2f" % reg.score(df_X_test, df_Y_test))

#UI
Sq_feet = input("Enter square footage:")
Bedrooms = input("Enter number of bedrooms:")

dict = {'GrLivArea': [Sq_feet], 'BedroomAbvGr': [Bedrooms]}
df_test = pd.DataFrame(dict)
eSalePrice=reg.predict(df_test)

print("Predicted Price:", "${:,.2f}".format(float(eSalePrice)))