# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:51:00 2019

@author: Samsung
"""

import pandas as pd
cars = pd.read_csv("cars.csv")
a = cars.iloc[0:5,[1,3,5,7,9,11]]
print(a,'\n')
print('------------------------ \n')

b = cars.loc[cars['Model']=='Mazda RX4',:]
print(b,'\n')
print('------------------------ \n')

c = cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]
print(c,'\n')
print('------------------------ \n')

d = cars.loc[(cars['Model']=="Mazda RX4 Wag") | (cars['Model']=="Ford Pantera L") | 
        (cars['Model']== "Honda Civic"),['Model','cyl','gear']]
print(d)




