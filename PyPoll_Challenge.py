import csv

total_votes = 0
candidates = []
candidate_votes = {}
counties = []
county_votes = {}
winning_candidate = ""
winning_count = 0

# Open the election results and read the file
with open('Resources/election_results.csv') as file:
    election_data = csv.reader(file)
    # Skip the header row in the CSV file.
    next(election_data)
    # Loop over the rows and add the votes to the total vote count.
    for row in election_data:
        total_votes += 1
        candidate = row[2]
        county = row[1]
        # If the candidate does not match any existing candidate, add to the candidate list and start tracking votes
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

        # If the county does not match any existing candidate, add to the county list and start tracking votes
        if county not in counties:
            counties.append(county)
            county_votes[county] = 1
        else:
            county_votes[county] += 1

# Get the candidate and county with the most votes
winning_candidate = max(candidate_votes, key=candidate_votes.get)
largest_county_turnout = max(county_votes, key=county_votes.get)

# Start adding text to the election_results variable
election_results = (f'''
Election Results
{'-' * 25}
Total Votes: {total_votes:,}
{'-' * 25}\n
County Votes:\n''')

# Loop over counties and add the votes to the election_results variable
for county in county_votes:
    county_data = f'{county}: {county_votes[county] / total_votes:.1%} ({county_votes[county]:,})\n'
    election_results += county_data

election_results += f'''
{'-' * 25}
Largest County Turnout: {largest_county_turnout}
{'-' * 25}
'''
# Loop over candidates and add the votes to the election_results variable
for candidate in candidate_votes:
    candidate_data = f'{candidate}: {candidate_votes[candidate] / total_votes:.1%} ({candidate_votes[candidate]:,})\n'
    election_results += candidate_data

election_results += f'''{'-' * 25}
Winner: {winning_candidate}
Winning Vote Count: {candidate_votes[winning_candidate]:,}
Winning Percentage: {candidate_votes[winning_candidate] / total_votes:.1%}
{'-' * 25}'''

# Save the election results to our text file.
with open('analysis/election_results.txt', 'w') as results_file:
    results_file.write(election_results)

# Print the election results to the terminal.
print(election_results)
