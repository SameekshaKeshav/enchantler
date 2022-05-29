#!/usr/bin/env python
# coding: utf-8

#uses cleanedSalesData when exists if not uses CleanSalesData.py to produce one and use it
#uses matplot library to produce the chart of Sales against power of the vehicle
#plot is exported as jpg file to the images folder
#browser is directed to show the image via the image tag from the enclosing php file that calls this function

import os
import numpy as np
import pandas as pd      #for data processing
import matplotlib.pyplot as plt     #for data visualization
import seaborn as sns
import os.path as path

file_exists = path.exists('./data/CleanedSalesData.csv')
if(file_exists):
    print("File exists")
else:
    print("File does not exist")
    import CleanSalesData
df_no_mv = pd.read_csv('./data/CleanedSalesData.csv')
df1 = df_no_mv[['Sales_in_thousands','Horsepower']]
df2 = df1.groupby('Horsepower')['Sales_in_thousands'].sum().reset_index(name ='Sales_in_thousands')

ypoints = np.array(df2['Sales_in_thousands'])
xpoints = np.array(df2['Horsepower'])
plt.figure(figsize =(14, 7))
sns.barplot(x=xpoints,y=ypoints,ci=None)
plt.xlabel("Horsepower")
plt.ylabel("Sales_in_thousands")
plt.xticks(rotation=90)
plt.savefig("./images/output.jpg")
   
