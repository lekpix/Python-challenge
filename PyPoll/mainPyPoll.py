import os
import csv
filepath=os.path.join('Resources','election_data.csv')
print(filepath)
with open(filepath,'r') as f :
   csv_reader=csv.reader(f,delimiter=',')
   Header_csv=next(csv_reader)#Skip Header
   Total_Votes=0
   #print(Header_csv)
   Cand_dict={}
   for row in csv_reader:
      #The total number of votes cast
      Total_Votes=Total_Votes+1
      if row[2] not in Cand_dict: #A complete list of candidates who received votes
         Cand_dict[row[2]] = 0
      Cand_dict[row[2]] = Cand_dict[row[2]] + 1 #The total number of votes each candidate won
   print(f'Election Results')
   print('---------------------------')
   print (f'Total votes : {Total_Votes}')
   print('---------------------------')
   old_value=0
   for key in Cand_dict:
      value=Cand_dict[key]
      if old_value <= value : #Calculating Winner of the election based on popular vote.
         old_value=value
         Winner=key
      Vote_Per=(value/Total_Votes)*100 #Calculating The percentage of votes each candidate won
      print(f'{key} : {"%.2f" % Vote_Per} % ({value})')
   print('---------------------------')
   print(f'Winner is {Winner}')
   print('---------------------------')
#opening a text file
import sys
sys.stdout = open('Analysis/ElectionResults.txt', 'w') 
print(f'Election Results')
print('---------------------------')
print (f'Total votes : {Total_Votes}')
print('---------------------------')
for key in Cand_dict:
   value=Cand_dict[key]
   Vote_Per=(value/Total_Votes)*100 #Calculating The percentage of votes each candidate won
   print(f'{key} : {"%.2f" % Vote_Per} % ({value})')
print('---------------------------')
print(f'Winner is {Winner}')
print('---------------------------')   