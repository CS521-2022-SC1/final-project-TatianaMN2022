# Home Price Calculator Version 0.01
# Importing pandas and numpy
import pandas as pd
import numpy as np

# Importing the data
scan = pd.read_csv('C:/Users/tatia/OneDrive/Documents/GitHub/final-project-TatianaMN2022/Data/House Prediction Data.csv')

# copying columns I will use into a new dataframe
df = scan[['GrLivArea','SalePrice']].copy()

# eliminating columns with blank values
modifieddf = df.dropna()

# Initial linear regression
# Code source: Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Split the data into training/testing sets
df_X_train = modifieddf[['GrLivArea']][:-20]
df_X_test = modifieddf[['GrLivArea']][-20:]


# Split the targets into training/testing sets
df_Y_train = modifieddf[['SalePrice']][:-20]
df_Y_test = modifieddf[['SalePrice']][-20:]

# Create linear regression object
reg = linear_model.LinearRegression()

# Train the model using the training sets

# starting with a single variable, x = GrLivArea and y = SalePrice


reg.fit(df_X_train, df_Y_train)

#print(modifieddf[['YrSold']].to_string())
#print(modifieddf.SalePrice.to_string())

# Make predictions using the testing set
# Defining the Estimated Sale Price = eSalePrice
#eSalePrice = reg.predict(2010)
#mask = modifieddf['GrLivArea'] == 2000
#eSalePrice = reg.predict(modifieddf.loc[mask, 'GrLivArea'].values.reshape(-1, 1))

#modifieddf_test=modifieddf[['GrLivArea']][-20:]
dict = {'GrLivArea': ['1000','8500']}
df_test = pd.DataFrame(dict)
d = ['1000','8500']



#testSalePrice=reg.predict(df_test)
eSalePrice=reg.predict(df_X_test)

print("Predicting for square footage: \n",df_X_test)
print("predicted price: \n",eSalePrice)
# The coefficients
print("Coefficients: \n", reg.coef_)
print("Intercept: \n", reg.intercept_)



plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
#plt.scatter(modifieddf.GrLivArea,modifieddf.SalePrice)
plt.scatter(df_X_test,df_Y_test)
plt.plot(df_X_test, eSalePrice, color="black", linewidth=3)
#plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)
plt.show()
# The mean squared error
#print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
#print("Mean squared error: %.2f" % mean_squared_error(modifieddf.SalePrice, eSalePrice))

#print("Mean squared error: %.2f" % mean_squared_error(modifieddf.SalePrice, eSalePrice))

# The coefficient of determination: 1 is perfect prediction
#print("Coefficient of determination: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
#plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
#plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

#plt.xticks(())
#plt.yticks(())

#plt.show()

