from operator import indexOf
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#list creation
totalmonths=[] 
net_total_pl=[]
changes_pl=[]
count=0

with open(csvpath) as file:  

    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)
    #print(header)

    for row in csvreader:
        count +=1
        totalmonths.append(row[0])
        net_total_pl.append(int(row[1]))

pl_delta=0
for i in range(len(net_total_pl)-1):
    pl_delta=net_total_pl[i+1]-net_total_pl[i]
    changes_pl.append(pl_delta)
#print(changes_pl)   

average_change=round(sum(changes_pl)/len(changes_pl), 2)
#print(average_change)

greatestinc=max(changes_pl)
greatestdec=min(changes_pl)
ginc_dex=changes_pl.index(max(changes_pl))
gdec_dex=changes_pl.index(min(changes_pl))
#print(greatestinc)
#print(greatestdec)

ginc_dt=totalmonths[ginc_dex+1]
#print(ginc_dt)
gdec_dt=totalmonths[gdec_dex+1]
#print(gdec_dt)

#printing summary
print(f"Financial Analysis")
print(f"--------------------------------")
print("Total Months: " + str(count))
print("Total: " + "$" + str(sum(net_total_pl)))
print("Average Change: " + "$" + str(average_change))
print("Greatest Increase in Profits: " + str(ginc_dt) + " $" + str(greatestinc))
print("Greatest Decrease in Profits: " + str(gdec_dt) + " $" + str(greatestdec))

txtpath = os.path.join("analysis","bank_analysis.txt")
with open(txtpath,"w") as txtfile:
        txtfile.write(f"Financial Analysis")
        txtfile.write(f"--------------------------------")
        txtfile.write("Total Months: " + str(count))
        txtfile.write("Total: " + "$" + str(sum(net_total_pl)))
        txtfile.write("Average Change: " + "$" + str(average_change))
        txtfile.write("Greatest Increase in Profits: " + str(ginc_dt) + " $" + str(greatestinc))
        txtfile.write("Greatest Decrease in Profits: " + str(gdec_dt) + " $" + str(greatestdec))