# Home Price Calculator

Home Price Calculator is a Python program that uses a linear regression model to predict the price of a home. 
Using data from SOURCE, it will estimate the price of a home upon your providing information about the home in the form of 3 inputs.

The Home Price Calculator was created for the final project in the course MET CS521, offered at Boston University.

## Requirements

Pandas
Numpy
Matplotlib
SKLearn

## Installation

?ask about this section

## Usage

Input VARIABLES FROM CORE MODEL:
MSSubClass: Identifies the type of dwelling involved in the sale.
MSZoning: Identifies the general zoning classification of the sale.
Neighborhood: Physical locations within Ames city limits
Condition1: Proximity to various conditions
Condition2: Proximity to various conditions (if more than one is present)
BldgType: Type of dwelling
OverallCond: Rates the overall condition of the house
YearBuilt: Original construction date
YearRemodAdd: Remodel date (same as construction date if no remodeling or additions)
CentralAir: Central air conditioning
GrLivArea: Above grade (ground) living area square feet
FullBath: Full bathrooms above grade
HalfBath: Half baths above grade
Bedroom: Bedrooms above grade (does NOT include basement bedrooms)
GarageCars: Size of garage in car capacity
PoolArea: Pool area in square feet

The output you will receive is the estimated price at the time of the sale.

## Core Model
The Home Price Calculator is based on the following models:

Versions 0.01 and 0.02 use a model that is based on 
 Initial linear regression
 Code source: Jaques Grobler
 License: BSD 3 clause

Version 0.03 uses a class with the following methods to perform data analysis and display:


```bash
 - set_independent_variables
 - print_independent_variables
 - do_regression
 - print_report
```

Output variable:
estimated SalePrice

Y variable to be analyzed:
SalePrice

X variables of interest, to be potentially analyzed:

MSSubClass: Identifies the type of dwelling involved in the sale.
MSZoning: Identifies the general zoning classification of the sale.
Neighborhood: Physical locations within Ames city limits
Condition1: Proximity to various conditions
Condition2: Proximity to various conditions (if more than one is present)
BldgType: Type of dwelling
OverallCond: Rates the overall condition of the house
YearBuilt: Original construction date
YearRemodAdd: Remodel date (same as construction date if no remodeling or additions)
CentralAir: Central air conditioning
GrLivArea: Above grade (ground) living area square feet
FullBath: Full bathrooms above grade
HalfBath: Half baths above grade
Bedroom: Bedrooms above grade (does NOT include basement bedrooms)
GarageCars: Size of garage in car capacity
PoolArea: Pool area in square feet
YrSold: Year Sold (YYYY)

## Methodology

This program utilizes a linear regression model, assessing the relationship of various explanatory variables with the output variable

## Additional Documents
In addition to the script, a written analysis is provided in the repository to further explain and explore the methods and outputs of this program.

## Collaborators
None

## License
None