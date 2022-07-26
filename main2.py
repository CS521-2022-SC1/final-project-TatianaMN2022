# Home Price Calculator Version 0.02
# Importing pandas and numpy
import pandas as pd
import numpy as np

# Importing the data
scan = pd.read_csv('C:/Users/tatia/OneDrive/Documents/GitHub/final-project-TatianaMN2022/Data/House Prediction Data.csv')

# copying columns I will use into a new dataframe
df = scan[['GrLivArea','BedroomAbvGr','SalePrice']].copy()

# eliminating columns with blank values
modifieddf = df.dropna()

# Initial linear regression
# Code source: Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Split the data into training/testing sets
df_X_train = modifieddf[['GrLivArea','BedroomAbvGr']][:-20]
df_X_test = modifieddf[['GrLivArea','BedroomAbvGr']][-20:]


# Split the targets into training/testing sets
df_Y_train = modifieddf[['SalePrice']][:-20]
df_Y_test = modifieddf[['SalePrice']][-20:]

# Create linear regression object
reg = linear_model.LinearRegression()

# Train the model using the training sets

# starting with a single variable, x = GrLivArea and y = SalePrice


reg.fit(df_X_train, df_Y_train)


# Make predictions using the testing set
# Defining the Estimated Sale Price = eSalePrice
'''
dict = {'GrLivArea': ['1000','8500']}
df_test = pd.DataFrame(dict)
d = ['1000','8500']
'''



eSalePrice=reg.predict(df_X_test)

print("Predicting for: \n",df_X_test)
print("predicted price: \n",eSalePrice)
# The coefficients
print("Coefficients: \n", reg.coef_)
print("Intercepter: \n", reg.intercept_)

'''
plt.xlabel('eSalePrice')
plt.ylabel('SalePrice')

plt.scatter(eSalePrice,df_Y_test)
plt.plot(df_X_test, eSalePrice, color="black", linewidth=3)

plt.show()
'''
#UI
Sq_feet = input("Enter square footage:")
Bedrooms = input("Enter number of bedrooms:")

dict = {'GrLivArea': [Sq_feet], 'BedroomAbvGr': [Bedrooms]}
df_test = pd.DataFrame(dict)
eSalePrice=reg.predict(df_test)

print("Predicted Price:", "${:,.2f}".format(float(eSalePrice)))


