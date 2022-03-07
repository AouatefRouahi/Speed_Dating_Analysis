#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from datetime import datetime
import pandas as pd
import numpy as np


def explore(dataset):
    print("Shape : {}".format(dataset.shape))
    print()

    print("data types : \n{}".format(dataset.dtypes))
    print()

    print("Display of dataset: ")
    display(dataset.head())
    print()

    print("Basics statistics: ")
    display(dataset.describe(include='all'))
    print()

    print("Distinct values: ")
    display(pd.Series(dataset.nunique(dropna = False)))


def unique_count(dataset, Cols):
    for col in Cols:
        print(f"unique values of {col}:")
        display(dataset[col].value_counts(dropna=False, ascending=False))


def missing(dataset):
    '''
        This function return a dataFrame that contains information on 
        the number and the proportion of missing values in a given dataset
        It excludes columns that do not contain missing values
    '''
    missing = pd.DataFrame(columns=['Variable', 'n_missing', 'p_missing'])

    miss = dataset.isnull().sum() # series

    missing['Variable'] = miss.index
    missing['n_missing'] = miss.values
    missing['p_missing'] = round(100*miss/dataset.shape[0],2).values
    mask = missing['n_missing'] == 0
    missing = missing[~mask]

    return missing.sort_values(by='n_missing', ascending=False)  


def duplicates_count(dataset):
    count_dup = len(dataset)-len(dataset.drop_duplicates())
    if count_dup == 0:
        print('No duplicated rows found')
    else: 
        display(
            df.groupby(df.columns.tolist())\
              .size().reset_index()\
              .rename(columns={0:'records'}))


def outliers_count(dataset, columns):
    index = ['count', 'mean', 'std', 'low_fence', 'high_fence', 'outliers', 'count_after_drop']
    df_outliers = pd.DataFrame(columns= columns, index = index)
    for col in columns:
        count = dataset[col].count()
        mean = dataset[col].mean()
        std = dataset[col].std()
        low_fence = mean - 3 * std
        high_fence =  mean + 3 * std

        mask = (dataset[col] < low_fence) | (dataset[col] > high_fence)
        outliers = dataset[col][mask].count()
        count_after_drop = count - outliers

        df_outliers[col] = [count, mean, std, low_fence, high_fence, outliers, count_after_drop]

    display(df_outliers)


def remove_outlier(dataset, col):
    mean = dataset[col].mean()
    std = dataset[col].std()
    low_fence  = mean - 3 * std
    high_fence = mean + 3 * std
    mask = (dataset[col] < low_fence)| (dataset[col] > high_fence)
    df_out = dataset.loc[~mask]
    return df_out


def remove_missing(dataset, col):      
    mask = dataset[col].isna()
    df_out = dataset.loc[~mask]

    return df_out
