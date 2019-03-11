# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:11:59 2018

@author: hello
"""

import os
import csv
from datetime import datetime
budgetdataCSV = os.path.join('C:/Users/hello/Desktop/python-challenge/PyBank/budget_data.csv')
with open(budgetdataCSV, 'r') as csvfile:
    
    # Split the data on commaas
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    row_count = sum(1 for r in reader)    
    print("Total Months: " + str(row_count))
        
    csvfile.seek(0)
    next(reader)
      
    csvfile.seek(0)
    next(reader)
    
    avgdifflist = []
    prev = 0
    profit_loss = 0   
    for x in reader:
        profit_loss = profit_loss + int(x[1])
        avgdiff =int(x[1])-prev 
        prev = int(x[1])
        avgdifflist.append(avgdiff)
        length  = len(avgdifflist)-1
        
    total_avg = sum(avgdifflist[1:]) / length
        
    print("Total: $" +str(profit_loss))
    print("Average Change: $" +str(total_avg))
    print("Greatest Increase in Profits: (" + str(max(avgdifflist)) + ")")
    print("Greatest Decrease in Profits: (" + str(min(avgdifflist)) + ")")
    
   #Total Months: 86
   #Total: $38382578
   #Average Change: $-2315.1176470588234
   #Greatest Increase in Profits: (1926159)
   #Greatest Decrease in Profits: (-2196167)