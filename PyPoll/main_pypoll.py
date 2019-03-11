# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 18:37:06 2018

@author: hello
"""

import os
import csv
from datetime import datetime
electiondataCSV = os.path.join('C:/Users/hello/Desktop/python-challenge/PyPoll/election_data.csv')
with open(electiondataCSV, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
  #  row_count = sum(1 for r in reader)    
  # print("Count of votes: " + str(row_count))
  
    total_votes = 0 
    candidates_list = []
    candidate_count = {}
   
    for x in reader:
        total_votes = total_votes + 1
    
    
        if x[2] not in candidates_list:
            candidates_list.append(x[2])
                  
            candidate_count[x[2]] = 0
        candidate_count[x[2]] = candidate_count[x[2]]+1
        
    candidate_count_percent = {}
    for k in candidate_count:
        candidate_count_percent[k] = (candidate_count[k]/total_votes) * 100
    #print(candidate_count_percent)
    winner = list(candidate_count_percent.keys())[list(candidate_count_percent.values()).index(max(candidate_count_percent.values()))]
        
    
    print("Total Votes: " +str(total_votes))
    print("Candidate List: " +str(candidates_list))
    print("Candidate Count: {" + str(candidate_count) + "}")
    print("Candidate Vote Percentage: {" + str(candidate_count_percent)+ "}")
    print("Winner: (" + str(winner) + ")")
    
    
#Total Votes: 3521001
#Candidate List: ['Khan', 'Correy', 'Li', "O'Tooley"]
#Candidate Count: {{'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}}
#Candidate Vote Percentage: {{'Khan': 63.00001050837531, 'Correy': 19.999994319797125, 'Li': 13.999996023857989, "O'Tooley": 2.999999147969569}}
#Winner: (Khan)   
   
