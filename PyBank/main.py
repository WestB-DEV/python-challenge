#1 import os and the csv file in quesiton
import os
import csv
#read and write filepath
csvpath = os.path.join("Resources", "budget_data.csv")
csv_out= os.path.join("analysis", "budget_analysis.txt")

#make the variables for the for loop that will return the final answers
#Your first variable will include the total months in the CSV 
months=0
#your second variable the net total profit
netprofit=0
#make a variable to store the dictionary of changes month to month. The order will not matter as we will be sorting them by value
changedict={}
#make variables to store the greatest increase, decrease and corresponding dates (could have been a dictionary or list)
greatestincrease_val=0
greatestdecrease_val=0
greatest_increase=""
greatest_decrease=""
#store the sum of the changes month to month
month_delta=0
#make another variable to store the value associated with each month (for use in the for loop later)
prevmonth=0
#open the csv and make a variable to call the csv reader
with open(csvpath, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row
    # go through the rest of the rows and add to the count for each row
    for row in csvreader:
        months = months +1
        #calculate the change per month and store it in the list
        month_income=int(row[1])
        month_name=str(row[0])
        #iterate through the 2nd column and add each value to the previous value
        netprofit=(month_income+netprofit) #iterate through the 2nd column and add each value to the previous value
        #target the month's name that was just captured and assign it a value equal to the difference between the current month and the previous month
        changedict[month_name]= month_income-prevmonth
        #set the value of the "prevmonth" variable to be ready for the next loop
        prevmonth= month_income
#iterate throught the key, value pairs in the changedict dictionary (touple) 
for key, value in changedict.items(): #(source for this technique https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops)
    #for the purposes of finding average change, start adding the deltas together
    month_delta=month_delta-value
    if value>greatestincrease_val:
        greatestincrease_val=value
        greatest_increase=key
    if value<greatestdecrease_val:
        greatestdecrease_val=value
        greatest_decrease=key
      
#use the sum of the deltas, plus the number of deltas to find the average. Make that a variable
finalmonthdelta=month_delta/months
 
 #take the variables and make a print statement to go to a new file  
output = (
    "Financial Analysis\n"
    "--------------------------------------\n"
    f"Total months: {months}\n"
    f"Total: {netprofit}\n"
    f"Average change: {finalmonthdelta}\n"
    f"Greatest Increase in Profits: {greatest_increase} (${greatestincrease_val})\n"
    f"Greatest Decrease in Profits: {greatest_decrease} (${greatestdecrease_val})\n"
)

# Print the results to the terminal
print(output)

# Write the results to csv_out
with open(csv_out, "w") as txt_file:
    txt_file.write(output)
