# Import os module with proper functions
import os
#Module/reading CSV files
import csv

#Appending file directory
filepath = os.path.join("..",'Resources','election_data.csv')

#variables
Totalcount = 0; Kcount = 0; Ccount = 0; lCount = 0; oCount = 0; Max_votecount = 0

#Percentage calculation
def percentage (part, whole):
    return 100 * float(part)/float(whole)

#Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for i in csvreader:
         Voterid = i[0]
         country = i[1]
         Candidate = i[2]
         #Searching for total Vote Count
         Totalcount = Totalcount + 1

         #Searching for votecount by candidates
         if Candidate =="Khan": Kcount = Kcount + 1
         if Candidate =="Correy": Ccount = Ccount + 1
         if Candidate =="Li": lCount = lCount + 1
         if Candidate =="O'Tooley": oCount = oCount + 1
            
# Defining the dictionary (list) for the candidate and votes
     candidatevote = {"Khan": Kcount,"Correy": Ccount,"Li" :lCount, "O'Tooley": oCount}
     #searching for winner 
     for Candidate, value in candidatevote.items():
         if value > Max_votecount: 
            max_votecount = value 
            winner = Candidate

#Printing results       
print(f'Election Results'+'\n')
print(f'-------------------------------'+'\n')
print(f'Total Votes: {Totalcount}'+'\n')
print(f'-------------------------------'+'\n')

print(f'Khan: {percentage(Kcount,Totalcount):.3f}%  ({Kcount})')
print(f'Correy: {percentage(Ccount,Totalcount):.3f}%  ({Ccount})')
print(f'Li: {percentage(lCount,Totalcount):.3f}%  ({lCount})')
print(f'O\'Tooley: {percentage(oCount,Totalcount):.3f}%  ({oCount})')
print(f'--------------------------------'+'\n')
print(f'Winner: {winner} '+'\n')
print(f'--------------------------------'+'\n')