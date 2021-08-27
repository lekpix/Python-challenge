import os
import csv
filepath=os.path.join('Resources','budget_data.csv')
#print(filepath)
with open(filepath,'r') as f :
    csv_reader=csv.reader(f,delimiter=',')
    Count_Months=0
    Total_Profit_Loss=0
    Total_change=0.0
    Avg_cntr=0
    Old_Profit_Loss=0.0
    Grt_Inc=0.0
    Grt_Dec=0.0
    Header_csv=next(csv_reader)#Skip Header
    for row in csv_reader:
        Date_period=row[0]
        Curr_Profit_Loss=float (row[1])
        Count_Months=Count_Months+1#Count number of Months
        Total_Profit_Loss=Total_Profit_Loss+Curr_Profit_Loss#Total Profit Loss
        #Calculating total change
        if Old_Profit_Loss!=0 :#Skipping the first value
            Curr_Change=Curr_Profit_Loss-Old_Profit_Loss
            Total_change=(Curr_Change)+Total_change#Calculating Total Change
            if Curr_Change!=0 :
                Avg_cntr=Avg_cntr+1
            #Calculating Greatest Increase in Profits:
            if Curr_Change >=Grt_Inc :
                Grt_Inc=Curr_Change
                Date_Inc=Date_period
            #Calculating Greatest Decrease in Profits:
            if Curr_Change <=Grt_Dec :
                Grt_Dec=Curr_Change   
                Date_Dec=Date_period
        Old_Profit_Loss=Curr_Profit_Loss
    #Calculating the average Change
    Average_change=Total_change/Avg_cntr
    print('Financial Analysis')
    print(f'Total Months : {Count_Months}')
    print(f'Total Profit/Loss : ${Total_Profit_Loss}')
    print(f'Average change : ${"%.2f" % Average_change}')
    print(f'Greatest Increase in Profits:{Date_Inc}  (${Grt_Inc})')
    print(f'Greatest Decrease in Profits:{Date_Dec} (${Grt_Dec})')
#opening a text file
import sys
sys.stdout = open('Analysis/FinancialAnalysis.txt', 'w')
print('Financial Analysis')
print(f'Total Months : {Count_Months}')
print(f'Total Profit/Loss : ${Total_Profit_Loss}')
print(f'Average change : ${"%.2f" % Average_change}')
print(f'Greatest Increase in Profits:{Date_Inc}  (${Grt_Inc})')
print(f'Greatest Decrease in Profits:{Date_Dec} (${Grt_Dec})')



