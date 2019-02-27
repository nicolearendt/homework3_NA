import os
import csv

#path to budget data
csvpath = os.path.join("Resources", "budget_data.csv")

print()
print("Financial Analysis")
print("------------------------")

#get the total number of months by counting each row (after the header)
def getMonthTotal():
    month = sum(1 for row in csvreader)
    return month

#get the net total amount of the profits/losses
def getNetTotal():
    total = 0
    for row in csvreader:
        total += int(row[1])
    return total
    
def getAvg():
    profits= []
    for row in csvreader:
        profits.append(int(row[1]))
    change = []
    for i in range(len(profits) - 1):
        change.append(profits[i+1] - profits[i])
    avg = sum(change)/len(change)
    return avg



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    mtotal = getMonthTotal()
    print(f"Total Months: {mtotal}")
    
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    ntotal = getNetTotal()
    print(f"Total: ${ntotal}")
    
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    avgChange = round(getAvg(),2)
    print(f"Average Change: ${avgChange}")