# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:28:39 2019

@author: Samsung
"""

import pandas as pd
cars = pd.read_csv("cars.csv")
firstFive = cars.head()
print(firstFive, '\n')
lastFive = cars.tail()
print(lastFive)