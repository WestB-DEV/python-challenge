#1 import os and the csv file in quesiton
import os
import csv
#read and write filepath
csvpath = os.path.join("/Users/gowest/uci/homework/Challenge 3 /Starter_Code 6/PyPoll/Resources/election_data.csv")
txt_out= os.path.join("/Users/gowest/uci/homework/Challenge 3 /Starter_Code 6/PyPoll/output/pollresults.txt")

#define variables outside of the for loops
vote_total=0
canidates=[]
canidate_totals={}
most_votes=0
winner=""
final_message=[]

#Open the csv with read permission/mode
with open(csvpath, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row
    
    # go through the rest of the rows and add to the count for each row
    for row in csvreader:
        
        #add 1 vote to the total count per row
        vote_total+=1
        
        #define how to look for names
        names=str(row[2])
        
        #check if names are in the candidates list, if not, add them to the list and +1 the vote count
        if names not in canidates:
            canidates.append (names)
            canidate_totals[names]= 0
            canidate_totals[names]= canidate_totals[names]+1
        
        #if the name matches the inside of the list, add to the exsisting vote count
        elif names in canidates:
           canidate_totals[names]= canidate_totals[names]+1

#at the end of the first loop, loop again through the newly created dictinary
for canidates in canidate_totals:
    
    #for each canidate, this loop will pull the total votes for each canidate
    ind_votes=canidate_totals.get(canidates)
   
    #check the individual votes against the winning number of votes and update that number if it encounters a higher number
    if ind_votes>most_votes:
        most_votes=ind_votes
    
    #divide to find their alloted percent of the total vote
    percent=float(ind_votes)/float(vote_total)*100
    
    #then print out the results
    print (f"{canidates} earned {ind_votes} votes, which is {round(percent)}% of the total vote count")
    
    #append the message to the final message list for printing into the final txt file
    final_message.append(f"{canidates} earned {ind_votes} votes, which is {round(percent)}% of the total vote count\n\n")


#loop through the dictionary 1 more time to find the winning canidate
for canidates in canidate_totals:
    ind_votes=canidate_totals.get(canidates)
    if ind_votes==most_votes:
        winner=canidates
        print(f"your winner is {winner} ")


#send results to the txt file

with open(txt_out, "w") as txt_file:
    txt_file.write(f"Election results\n\n-------------------------\n\nTotal Votes: {vote_total}\n\n-------------------------\n\n{final_message}\n\n-------------------------\n\nYour winner is {winner}")
