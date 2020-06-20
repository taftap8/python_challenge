#get CSV file
import os
import csv
import statistics

#read/write CSV File
csvpath = os.path.join("PyPoll.csv")


with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #remove header from calculation
    header=next(csvreader)