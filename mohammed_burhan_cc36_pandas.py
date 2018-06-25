# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:05:24 2018

@author: Lenovo
"""


import pandas as pd
df=pd.read_csv("training_titanic.csv")
df["Child"] = 0
df["Child"][df["Age"] < 18] = 1
df["Child"][df["Age"] >= 18] = 0
df["Survived"][df["Child"] == 1].value_counts(normalize = True)


