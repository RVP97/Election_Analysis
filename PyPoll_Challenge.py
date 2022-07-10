import csv

total_votes = 0
candidates = []
candidate_votes = {}
counties = []
county_votes = {}
winning_candidate = ""
winning_count = 0

with open('Resources/election_results.csv') as file:
    election_data = csv.reader(file)
    next(election_data)
    for row in election_data:
        total_votes += 1
        candidate = row[2]
        county = row[1]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

        if county not in counties:
            counties.append(county)
            county_votes[county] = 1
        else:
            county_votes[county] += 1

winning_candidate = max(candidate_votes, key=candidate_votes.get)
largest_county_turnout = max(county_votes, key=county_votes.get)

election_results = (f'''
Election Results
{'-' * 25}
Total Votes: {total_votes:,}
{'-' * 25}\n
County Votes:\n''')

for county in county_votes:
    county_data = f'{county}: {county_votes[county] / total_votes:.1%} ({county_votes[county]:,})\n'
    election_results += county_data

election_results += f'''
{'-' * 25}
Largest County Turnout: {largest_county_turnout}
{'-' * 25}
'''

for candidate in candidate_votes:
    candidate_data = f'{candidate}: {candidate_votes[candidate] / total_votes:.1%} ({candidate_votes[candidate]:,})\n'
    election_results += candidate_data

election_results += f'''{'-' * 25}
Winner: {winning_candidate}
Winning Vote Count: {candidate_votes[winning_candidate]:,}
Winning Percentage: {candidate_votes[winning_candidate] / total_votes:.1%}
{'-' * 25}'''

with open('analysis/election_results.txt', 'w') as results_file:
    results_file.write(election_results)

print(election_results)
