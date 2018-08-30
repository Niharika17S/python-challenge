# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 19:11:46 2018

@author: hello
"""

import os
import csv
budgetdataCSV = os.path.join('C:/Users/hello/Desktop/python-challenge/PyBank/budget_data.csv')
with open(budgetdataCSV, 'r') as csvfile:
    
    # Split the data on commaas
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    data = []
    for row in reader:
        months = sum(1 for r in reader) 
        print(months)