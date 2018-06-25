# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:44:09 2018

@author: Lenovo
"""

import pandas as pd
df=pd.read_csv("training_titanic.csv")



df["Survived"][df["Sex"] == 'male'].value_counts()


df["Survived"][df["Sex"] == 'female'].value_counts()

df["Survived"][df["Sex"] == 'male'].value_counts(normalize = True)
df["Survived"][df["Sex"] == 'female'].value_counts(normalize = True)