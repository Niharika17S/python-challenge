# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 11:11:18 2018

@author: hello
"""

import os
import csv
budgetdataCSV = os.path.join('../Resources/budget_data.csv')
with open(budgetdataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
    print(f"CSV Header: {header}")
    
         
        months=list(reader)
        row_count = len(months)
        print(row_count)
        
        
         #row_count = sum(1 for row in csvreader)
    #print(row_count if row_count else 'Empty')
    
    # data = len(list(csvreader))
       
        #print(data)