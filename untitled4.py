# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:54:20 2018

@author: Lenovo
"""

df["Child"][df["Age"] == 1 ].value_counts(normalize = True)

df["Child"][df["Age"] == 0].value_counts(normalize = True)
df["Survived"][df["Child"] == 1].value_counts(normalize = True)
df["Survived"][df["Sex"] == 'male'].value_counts(normalize = True)
df["Child"].value_counts()