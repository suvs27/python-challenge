#PyBank
import os
import csv

# Lists to store data
date = []
profit_losses = []

#read csv file
#path to the .py file 
print(os.path.dirname(__file__))
#chdir to one level up above the py file
os.chdir(os.path.dirname(__file__))
#sets the path to the data or csvfile and stores the path in a variable
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
#print(csvpath)
#opens csvfile and reads it
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    header = next(csvfile)
    #print(f"Header: {header}")
    
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(float(row[1]))
    #print(date)
    #print(profit_losses)

#The total number of months included in the dataset
total_months = int(len(date))
#print(total_months)

# The net total amount of "Profit/Losses" over the entire period
total_profit_loss = 0.0
for amount in profit_losses:
    total_profit_loss += amount
#print(total_profit_loss)

#The average of the changes in "Profit/Losses" over the entire period
sum_changes = 0.0
greatest_increase_profits = 0.0
greatest_decrease_profits = 0.0
sum_changes_2 =[]
for i in range(0, (len(profit_losses)-1)):
    sum_changes = sum_changes + ((profit_losses[i+1]) - (profit_losses[i]))
    #print(profit_losses[i+1])
    #print(profit_losses[i])
    #sum_changes_2.append((profit_losses[i+1]) - (profit_losses[i]))
    if (profit_losses[i+1]) - (profit_losses[i]) > greatest_increase_profits:
        greatest_increase_profits = (profit_losses[i+1]) - (profit_losses[i])
        greatest_increase_profit_month = date[i+1]

    if (profit_losses[i+1]) - (profit_losses[i]) < greatest_decrease_profits:
        greatest_decrease_profits = (profit_losses[i+1]) - (profit_losses[i])
        greatest_decrease_profit_month = date[i+1]
    #print(sum_changes_2)
#print(sum_changes)
#print(sum_changes_2)
average_change = round((sum_changes/(len(profit_losses)-1)),2)
#print(average_change)
#print(greatest_increase_profits)
#print(greatest_increase_profit_month)
#print(greatest_decrease_profit_month)

#Print output to terminal 
#```text
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f" Greatest Increase in Profits: {greatest_increase_profit_month} ${greatest_increase_profits}")
print(f" Greatest Decrease in Profits: {greatest_decrease_profit_month} ${greatest_decrease_profits}")

# Specify the file to write to
output_path = os.path.join("..", "output", "PyBank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
file = open("PyBank.txt","w")
file.write("----------------------------\n")
file.write("Financial Analysis \n")
file.write("----------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${total_profit_loss}\n")
file.write(f"Average Change: ${average_change}\n")
file.write(f" Greatest Increase in Profits: {greatest_increase_profit_month} ${greatest_increase_profits}\n")
file.write(f" Greatest Decrease in Profits: {greatest_decrease_profit_month} ${greatest_decrease_profits}\n")
file.close()
    
   

    