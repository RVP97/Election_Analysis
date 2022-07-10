# Election_Analysis

## Project Overview
A Colorado Board of election employee has given you the following tasks to complete the election
audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the number of votes received by each candidate.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.10.4, Visual Studio Code

## Summary
The analysis of the election showed that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette with 73.8% of the vote and 272,892 votes.

## Challenge Overview
There were several challenges that needed to be addressed for the analysis to be successful.
- A CSV had to be read in and parsed to obtain the data from the election, including the number of votes cast,
the candidates, and the votes received by each candidate
- A for loop was used to iterate through the data to calculate the total number of votes cast, the number of votes
- If statements were used to correctly add each vote to the correct candidate
- These data was stored in a dictionary for easy access
- The percentage of votes each candidate won was calculated by dividing the number of votes received by the total
- The final result summary was saved in a text file in a separate folder

## Challenge Summary
Creating a script that automatically generates a text file with the results of the election was the main challenge
addresses by the analysis. The script was created to be able to be run from the command line. Even though this project
was created with the congressional election in mind, it has the required portability to be used for other elections.