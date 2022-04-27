#from distutils import text_file
from operator import indexOf
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
#csvpath = os.path.join('\Users\bianc\OneDrive\Desktop\GitHub\python-challenge\pypoll\Resources\election_data.csv')
file_to_save = os.path.join("analysis","Election_analysis.txt")


totalvotes = 0
candidate_list = []
candidate_votes = {}


winning_candidate = ""
winning_count = 0

with open(csvpath,"r") as election_data:  

    csvreader = csv.reader(election_data, delimiter=',')
    header = next(csvreader)
    #print(header)

    for row in csvreader:
        totalvotes  = totalvotes  +1
        # Get candidate name
        candidateName = row[2]

        if candidateName not in candidate_list:
            # if name is not in the list, then add it to the list
            candidate_list.append(candidateName)

            # add the name and the vote score to a dictionoary eg {"Khan": 0, "Correy": 23}
            
            candidate_votes[candidateName]  = 0
        candidate_votes[candidateName]  += 1 



#print(candidate_votes)
winning_candidate =  max(candidate_votes, key = candidate_votes.get)
percentage_won = float(candidate_votes[winning_candidate]/totalvotes * 100)
#print(f"The winner is {winning_candidate}")
# print(f"The winning percentage is {percentage_won} " )

vote_final = []
for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes/totalvotes * 100)
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    vote_final.append(voter_output)
#print(voter_output)
#text_file.write(voter_output)


#for key in  candidate_votes.keys() :
    #print(f"{key}: {candidate_votes[key]}")

#print(voter_output)
#print(candidateName)
# with open(file_to_save, "w") as text_file:
#     Election_Result = (
#         f"--------------------------------\n"
#         f"Total Votes: {totalvotes}\n"
#         f"--------------------------------\n"
#         f"voter_output: {voter_output:,}\n"
#         f"--------------------------------\n"
#         f"Winner: {winning_candidate}")
#     print(Election_Result, end="")

# text_file.write(Election_Result)

print(f"Election Results")
print(f"--------------------------------")
print("Total Votes: " + str(totalvotes))
print(f"--------------------------------")
print(vote_final[0])
print(vote_final[1])
print(vote_final[2])
print(vote_final[3])
print(f"--------------------------------")
print(f"Winner: {winning_candidate}")

txtpath = os.path.join("analysis","vote_analysis.txt")
with open(txtpath,"w") as txtfile:
        txtfile.write(f"Election Results")
        txtfile.write(f"--------------------------------")
        txtfile.write("Total Votes: " + str(totalvotes))
        txtfile.write(f"--------------------------------")
        txtfile.write(vote_final[0])
        txtfile.write(vote_final[1])
        txtfile.write(vote_final[2])
        txtfile.write(vote_final[3])
        txtfile.write(f"--------------------------------")
        txtfile.write(f"Winner: {winning_candidate}")