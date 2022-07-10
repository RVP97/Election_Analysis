import csv

total_votes = 0
candidates = []
candidate_votes = {}
counties = []
county_votes = {}


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

print(total_votes)
print(candidates)
print(candidate_votes)
print(counties)
print(county_votes)

