import os
import csv

# Working directory
csv_path = os.path.join('C:\\Users\\cherr\\OneDrive\\Desktop\\Data Analytics UWA course\\Homework\\Week 3\\Module 3 Challenge\\PyPoll\\Resources\\election_data.csv')

# Declaring variables
total_votes = 0
candidate_votes = {}

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        # Total Votes
        total_votes += 1

        # Votes per candidate
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Print the election results
print(f'Election Results' + '\n')
print(f'----------------------------' + '\n')
print(f"Total Votes: {total_votes}")

# Calculate and print the percentage of votes for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Find the winner
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
