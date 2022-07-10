# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("../Election_Analysis/Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.

total_votes = 0
candidate_options = []
candidate_votes = {}

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    winning_count = 0
    winner_name = ''
    for name, votes in candidate_votes.items():
        print(f'{name}: {votes:,} ({(votes/total_votes):.1%})')
        if votes > winning_count:
            winning_count = votes
            winner_name = name
print(f'''
-------------------------
Winner: {winner_name}
Winning Vote Count: {winning_count:,}
Winning Percentage: {(winning_count / total_votes):.1%}
-------------------------''')