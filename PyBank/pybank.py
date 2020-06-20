#get CSV file
import os
import csv
import statistics

#read/write CSV File
csvpath = os.path.join("pybank.csv")


with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #remove header from calculation
    header=next(csvreader)
    #find first row of data
    firstrow = next(csvreader)
    months = 1
    profloss = 0
    prev_net= int(firstrow[1])
    #store calculation between months
    net_change_list = []
    #define list to set starting variables [str, 0]
    greatest_increase = ["",0]
    greatest_decrease = ["",0]
#define function to read file
    for x in csvreader:
        months += 1
        profloss = profloss + int(x[1])
        net_change = int(x[1]) - prev_net
        prev_net = int(x[1])
        net_change_list += [net_change]
        #store greatest increase and decrease in their lists
        if net_change > greatest_increase[1]:
            greatest_increase[0] = x[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = x[0]
            greatest_decrease[1] = net_change
    #calculate statistics
    mean = round(statistics.mean(net_change_list))
    #print values   
    print(f'Total Months: {months}')
    print(f' Total: {profloss}')
    print(f' Average Change: ${mean} ')
    print(f' Greatest Increase in Profits:  {greatest_increase[0]} (${greatest_increase[1]})')
    print(f' Greatest Deacrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')

#write to text file

filename = 'pybank.txt'
with open(filename, 'w') as file_object:
    file_object.write(f'Total Months: {months}\n')
    file_object.write(f' Total: {profloss}\n')
    file_object.write(f' Average Change: ${mean} \n')
    file_object.write(f' Greatest Increase in Profits:  {greatest_increase[0]} (${greatest_increase[1]})\n')
    file_object.write(f' Greatest Deacrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n')
