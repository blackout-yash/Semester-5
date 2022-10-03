# -*- coding: utf-8 -*-

# -- Sheet --

# importing the basic packages of Python and dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")
df.head()

# getting the details of raw Housning Data
df.info()

# Getting the first 10 rows of the dataset
df.head(10)

# Get the basic statistical summary of the variables present in the given raw data
df.describe()

# Getting its dimension
df.shape

# obtain the missing values present in the given raw Housing Data
df.isnull().sum()

# Six variables among them, having 20 missing values in each case
# Approximately, 4 percent observations in each variable has missing values
(20/506)*100

# getting the column names of the dataset
df.columns



# Importing the visualization package of Python
import matplotlib.pyplot as plt
import seaborn as sns
# Detection of outliers among all variables

%matplotlib inline
plt.subplots(figsize=(17,10))
df.boxplot(patch_artist=True, sym="k.")
plt.xticks(rotation=90)

# Variables containing Missing values are
# "CRIM", "ZN" , "INDUS", "CHAS", "AGE", "LSTAT"
# ..............................................
# Variables containing Outliers
# Numerical Variables: "CRIM", "ZN" , "RM", "DIS", "PTRATIO", "B", "LSTAT","MEDV"

# At first, we will go with the treatment of missing values and then after outliers.
# Now, The treatment of the missing values on the basis of the presence of the Outliers.
# There are six variables containing missing values.
# 
# ***PHASE 1: TREATMENT OF MISSING VALUES***
# 
# ***Separate all six variables contain missing values into three groups on the basis of the presence of outliers.***
# 1. cat_mv = Categorical variable conatining missing values (Missing values will be treated with ***mode***)--- "CHAS"
# 2. num_mv_out = Numerical variables containing missing values and outliers too (Missing values will be treated with ***median***)--- "CRIM", "ZN" ,"LSTAT"
# 3. num_mv_noOut = Numerical variables containing missing values but "no outliers" (Missing values will be treated with ***mean***)--- "INDUS", "AGE"
#    
# ***Initiate the treatment of Missing Values***


# For first category: "cat_mv_out"
cat_mv = pd.concat([df["CHAS"]],axis=1)
cat_mv

cat_mv.isnull().sum()

cat_mv.mode()

# Replacing the missing values with mode(value 0) to this categorical variable
# replace nan value to zero(mode = 0)
cat_mv.replace(np.nan, 0, inplace=True)

# After replacing with mode(Value = 0), now there is no missing values in this categorical variable
cat_mv.isnull().sum()

# dimension (506 Observations and 1 column)
cat_mv.shape

# For the second category: "num_mv_out" means Numerical variables containing missing values and outliers too
num_mv_out = pd.concat([df["CRIM"], df["ZN"], df["LSTAT"]],axis=1)

num_mv_out.isnull().sum()

# Each variable has missing values equal to 20 obs


num_mv_out.describe()

# Replacing the missing values with median of its variables ("num_mv_out")
num_mv_out = num_mv_out.fillna(num_mv_out.median())

# Now, "num_mv_out" has no missing values
num_mv_out.isnull().sum()

num_mv_out.shape

# For the third category: "num_mv_noOut" means Numerical variables containing missing values but "no outliers"
num_mv_noOut = pd.concat([df["INDUS"], df["AGE"]],axis=1)

num_mv_noOut

num_mv_noOut.isnull().sum()

# Each variable has missing values equal to 20 obs


# Replacing the missing values with mean of its variable ("num_mv_noOut")
# this category doesn't have outliers but having missing values in the two variables
num_mv_noOut = num_mv_noOut.fillna(num_mv_noOut.mean())

# Now, this cateory ("num_mv_noOut") has no missing values
num_mv_noOut.isnull().sum()

# ***PHASE 2: TREATMENT OF OUTLIERS*** 
# 
# ***After treatment of missing values, the dataset will have only outliers problems. So, the next treatment will be for outliers. Now, assign a dataset that will contain all 14 variables including the above three category ("Treated Missing Values" Variables). Finally, split this dataset into three categories. But the thing is, Only the first category will be focussed here because the first category contains outliers. The second and third categories have no outliers.***
# 1. num_out = Numerical variables containing outliers (Missing values will be treated with ***median***)--- "CRIM", "ZN", "RM", "DIS", "PTRATIO", "B", "LSTAT", "MEDV"
# 2. num_noOut = Numerical variables containing "no outliers" (Missing values will be treated with ***mean***)--- "INDUS", "NOX", "AGE", "RAD", "TAX"
# 3. cat_out = Categorical variable conatining no outliers --- "CHAS"---- In this variable, the observation is either 1 or 0


# For assigning or concatenating all the variables including with six treated missing values variables into a dataset
df1 = pd.concat([cat_mv,num_mv_out, num_mv_noOut, df["RM"], df["DIS"], df["PTRATIO"], df["B"], df["MEDV"], df["NOX"], df["RAD"], df["TAX"]],axis=1)

df1

# No missing values after merging all variables
df1.isnull().sum()

# Boxplot for all variables
plt.subplots(figsize=(17,10))
df1.boxplot(patch_artist=True, sym="k.")
plt.xticks(rotation=90)

# Nine variables containing outliers and remain doesn't have outliers


# ***Now, It's time for treatment of outliers***
# 1. num_out = Numerical variables containing outliers (Missing values will be treated with ***median***)--- "CRIM", "ZN", "RM", "DIS", "PTRATIO", "B", "LSTAT", "MEDV"


num_out = pd.concat([df1["CRIM"], df1["ZN"], df1["RM"], df1["DIS"], df1["PTRATIO"], df1["B"], df1["LSTAT"], df1["MEDV"]],axis=1)

num_out

# Detecting outliers in "cat_out"
plt.subplots(figsize=(17,10))
num_out.boxplot(patch_artist=True, sym="k.")
plt.xticks(rotation=90)

# Getting the basic statistical summary of those variables containing outliers
num_out.describe()

# Detecting and Removing Outliers
# Inter Quartile Range (IQR) is the difference between the 3rd Quartile and the first Quartile
# The data points which fall below Q1 – 1.5 IQR or above Q3 + 1.5 IQR are outliers.
def detect_outlier(feature):
    Q1 = np.percentile(feature, 25)
    Q3 = np.percentile(feature, 75) 
    IQR = Q3 - Q1
    IQR *= 1.5
    minimum = Q1 - IQR 
    maximum = Q3 + IQR
    flag = False
    
    if(minimum > np.min(feature)):
        flag = True
    if(maximum < np.max(feature)):
        flag = True
    
    return flag

# Using tukey method to remove outliers. Whiskers are set at 1.5 times Interquartile Range (IQR). Any value beyond the acceptance range are considered as outliers. 
# 
# ***Replacing the outliers with the median value of that feature***
# 
# ***Why replacing with median value?***
# 
# As the mean value is highly influenced by the outliers, it is advised to replace the outliers with the median value.


def  remove_outlier(feature):
    Q1 = np.percentile(num_out[feature], 25)
    Q3 = np.percentile(num_out[feature], 75)
    IQR = Q3 - Q1
    IQR *= 1.5
    
    minimum = Q1 - IQR # the acceptable minimum value
    maximum = Q3 + IQR # the acceptable maximum value
    
    median = num_out[feature].median()
    
    num_out.loc[num_out[feature] < minimum, feature] = median
    num_out.loc[num_out[feature] > maximum, feature] = median

# taking all the column

num_out = num_out.iloc[:, : ]
for i in range(len(num_out.columns)): 
        remove_outlier(num_out.columns[i])

# In "num_out" matrix, it contains all varibles
num_out = num_out.iloc[:, : ]

num_out

# This shows that these are the variables from "num_out" which contain Outliers
for i in range(len(num_out.columns)):
    if(detect_outlier(num_out[num_out.columns[i]])):
        print(num_out.columns[i], "Contains Outlier")

# Removing the outliers
for i in range (3):
    for i in range(len(num_out.columns)):
        remove_outlier(num_out.columns[i])

# After removing outliers, the following boxplots of each variable from "num_out" show, they have no more outliers
plt.subplots(figsize=(17,10))
num_out.boxplot(patch_artist=True, sym="k.")
plt.xticks(rotation=90)

# Finally, concatenating all variables after treatment of outliers with those varibales that have no outliers into a dataset
final_df = pd.concat([num_out, df1["CHAS"], df1["INDUS"], df1["NOX"], df1["AGE"], df1["RAD"], df1["TAX"]],axis=1)

# # After treatment of missing values as well as outliers 
# # The dataset is now ready for further analysis


final_df

# Boxplot for the final dataset
plt.subplots(figsize=(17,10))
final_df.boxplot(patch_artist=True, sym="k.")
plt.xticks(rotation=90)

# Here, Correlation matrix shows:
# the relationship among explanatory variables as well as,
# the relationship between the dependent varibale with each of the explanatory variables
sns.pairplot(final_df)

# the heatmap also shows the same things and interpretations which earlier correlation matrix has been shown
fig, ax = plt.subplots(figsize=(17,10))
correlation_matrix = final_df.corr().round(2)
# annot = True to print the values inside the square
sns.heatmap(data=correlation_matrix, annot=True)

# correlation between these variables
print("PEARSON CORRELATION")
print(final_df.corr(method="pearson"))
sns.heatmap(final_df.corr(method="pearson"))
plt.savefig("heatmap_pearson_final.png")
plt.clf()
plt.close()

#scatter plot to see how these features RAD, RM ,DIS, LSTAT, NOX, AGE, TAX, INDUS vary with Target variable (MEDV)
plt.figure(figsize=(17,5))


features = ['LSTAT','NOX','AGE','TAX','RM','DIS','INDUS']
target = final_df['MEDV']

for i, col in enumerate(features):
    plt.subplot(1, len(features) , i+1)
    x = final_df[col]
    y = target
    plt.scatter(x, y, marker='o')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('MEDV')

