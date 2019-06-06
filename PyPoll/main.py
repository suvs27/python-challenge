#PyPoll
import os
import csv

# Lists to store data
vote = []


#read csv file
#path to the .py file 
print(os.path.dirname(__file__))
#chdir to one level up above the py file
os.chdir(os.path.dirname(__file__))
#sets the path to the data or csvfile and stores the path in a variable
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
#print(csvpath)
#opens csvfile and reads it
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    header = next(csvfile)
    #print(f"Header: {header}")

    for row in csvreader:
        vote.append(row[2])
        #print(vote)
    
    total_vote = int(len(vote))
    #print(total_vote)

    my_set = set(vote)
    unique_vote_list = list(my_set)
    #print("List of unique candidate names : ",unique_vote_list)

    name_counter = 0
    percent_vote = 0
    poll_dictionary = {}
    winner_counter1 = 0
    for candidate in unique_vote_list:
        for name in vote:
            if candidate == name:
                name_counter = name_counter + 1
                #print(name_counter)
        if name_counter > winner_counter1:
            winner_counter1 = name_counter
            winner = candidate
        percent_vote = name_counter / total_vote
        poll_dictionary.update({candidate:["{:.3%}".format(percent_vote),name_counter]})
        name_counter = 0

#determine
#print(poll_dictionary)
#print(winner)
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

#print to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_vote}")
print("-------------------------")
for key in poll_dictionary: print(key:value)
#print(poll_dictionary[0])
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
#```



