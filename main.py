# Home Price Calculator Version 0.011

# Import pandas, numpy, matplotlib, and sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


# Import the data from local .csv file, using pandas
    #It's commented out because user will not have access to my local file
#scan = pd.read_csv('C:/Users/tatia/OneDrive/Documents/GitHub/final-project-TatianaMN2022/Data/House Prediction Data.csv')

# Importing the data from a network request
scan = pd.read_csv('https://raw.githubusercontent.com/bursteinalan/Data-Sets/master/Housing/House%20Prediction%20Data.csv')


# Copy columns I will use into a new dataframe
df = scan[['GrLivArea','SalePrice']].copy()


# Eliminate rows with blank values
modifieddf = df.dropna()


# Split the data into training/testing sets
df_X_train = modifieddf[['GrLivArea']][:-20]
df_X_test = modifieddf[['GrLivArea']][-20:]

df_Y_train = modifieddf[['SalePrice']][:-20]
df_Y_test = modifieddf[['SalePrice']][-20:]


# Create linear regression object
reg = linear_model.LinearRegression()

# Train the model using the training sets
reg.fit(df_X_train, df_Y_train)

# Make predictions using the model
dict = {'GrLivArea': ['1000','8500']}
df_test = pd.DataFrame(dict)

# Define the output of the regression model (y-bar)
eSalePrice=reg.predict(df_X_test)

# Show the key statistics to evaluate the model
df_output = df_X_test.copy()
df_output["Predicted Price"] = eSalePrice
print("Predicted prices for tested square footage: \n",df_output)
print("Coefficients: \n", reg.coef_)
print("Intercept: \n", reg.intercept_)
# R^2: the proportion of the variance that's explained by the model
print("R^2-value: %.2f" % reg.score(df_X_test, df_Y_test))

# Create a scatterplot
plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
plt.scatter(df_X_test,df_Y_test)
plt.plot(df_X_test, eSalePrice, color="black", linewidth=3)
plt.show()


