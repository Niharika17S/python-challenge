# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:11:59 2018

@author: hello
"""

import os
import csv
budgetdataCSV = os.path.join('C:/Users/hello/Desktop/python-challenge/PyBank/budget_data.csv')
with open(budgetdataCSV, 'r') as csvfile:
    
    # Split the data on commas
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    row_count = sum(1 for r in reader)    
    print("Total Months: " + str(row_count))
        
    csvfile.seek(0)
    next(reader)
    total = 0
    total = sum(int(row[1]) for row in reader)
    print("Total: " +str(total))
    
    csvfile.seek(0)
    next(reader)
    i = 1
    for avg in reader:
        total_average = int(avg[i+1])-int(avg[i])
        print("Average: " + str(total_average))    
    
    
    
    #average = total/row_count
    #print("Average:" + str(average))    