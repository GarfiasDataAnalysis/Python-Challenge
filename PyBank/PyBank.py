
# Import os module/functions
import os
#reading CSV files
import csv

#Appending file directory with file path
filepath = os.path.join( '..','Resources','budget_data.csv')

#Variables
Mcount = 0; Total = 0; preValue = 0; Dif = 0; DifMax = 0; DifMin = 0

#Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Budget Analysis'+'\n')
     print(f'----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         lAmount = int(Amount)
         Dif =  lAmount - preValue
         #Tracking greatest increase in profits 
         if DifMax < Dif: 
            DifMax = Dif 
            DifMaxDate = month
         #Tracking greatest decrease in profits
         if DifMin > Dif:
            DifMin = Dif
            DifMinDate = month

         preValue = lAmount   
         # Get total months
         Mcount = Mcount + 1
         Total += int(Amount) 

## Print Results ##      
#Total number of months included in the dataset
print(f'Total Months : {Mcount}')
#Total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {Total}')
# Greatest increase in profit
print(f'Greatest Increase in Profits: {DifMaxDate} : ($ {DifMax})')
# Greatest increase in profit
print(f'Greatest Decrease in Profits: {DifMinDate} : ($ {DifMin})')



