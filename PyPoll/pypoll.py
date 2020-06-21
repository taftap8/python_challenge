#get CSV file
import os
import csv

#read/write CSV File
csvpath = os.path.join("Resources","PyPoll.csv")


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #remove header from calculation
    header=next(csvreader)
    #print(header)
    #capture all votes
    totalVotes = 0
    #set list to capture candidates
    candidate_list = []
    #set dictionary to capture candidates votes
    candidate_votes = {}
    
    #loop through file to capture unique list of candidates and total votes per candidate
    for row in csvreader:
        totalVotes += 1
        candidate = row[2]
        if candidate not in candidate_list:
            #print(candidate)
            candidate_list.append(candidate)
            candidate_votes[candidate] = 1
            # candidate_list == candidate_votes.keys()
        else: 
            candidate_votes[candidate] += 1


    #print results
    print("Election Results")
    print("__________________________________________________________")
    print(f'Total Votes: {totalVotes}')
    print(f'_________________________________________________________')
    #loop through dict to display all values
    #found .get code for max key here https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    for candidate, votes in candidate_votes.items(): 
        percent_won = votes/ totalVotes *100    
        print(f'{candidate}: {percent_won} %')
        #print(f'{candidate}: {votes / totalVotes * 100}%')
    print(f'_________________________________________________________')
    print(f'Winner: {max(candidate_votes, key=candidate_votes.get)}')
    print(f'_________________________________________________________')
    
    #write to text file

    filename = 'Analytics/pypoll.txt'
    with open (filename, 'w') as file_object:
        file_object.write(f' Election Results\n')
        file_object.write(f'_________________________________________________________\n')
        file_object.write(f' Total Votes: {totalVotes}\n')
        file_object.write(f'_________________________________________________________\n')
        #loop through dict to display all values
        #found .get code for max key here https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        for candidate, votes in candidate_votes.items(): 
            percent_won = votes/ totalVotes *100    
            file_object.write(f'{candidate}: {percent_won} %\n')
        file_object.write(f'_________________________________________________________\n')
        file_object.write(f'Winner: {max(candidate_votes, key=candidate_votes.get)}\n')
        file_object.write(f'_________________________________________________________\n')
      