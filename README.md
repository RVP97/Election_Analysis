# Election_Analysis

## Project Overview
This project was born after a Colorado Board of election employee gave us the following tasks to complete the 
election  audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the number of votes received by each candidate.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

### Purpose
The purpose of the project was to systematically create a script that would be used to analyze the results of an
election in a swift manner.

## Resources
- Data source: election_results.csv
- Software: Python 3.10.4, ***PyCharm*** 2022.1.3

## Election-Audit Results
The analysis of the election showed that:
- There were **369,711** votes cast in the election.
  - The following code was used to calculate the total number of votes cast:
    ```python
    total_votes = 0
    for row in election_data:
        total_votes += 1
    ```
    - It was a simply yet effective way to loop over the data and calculate the total number of votes.
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
    - To get this list of counties, I used the following code:
      ```python
      for row in election_data:
          county = row[1]
            if county not in counties:
                counties.append(county)
                county_votes[county] = 1
      ```
      - This added the county to the county list and set the initial vote count to 1 if it was not already in the list.
- The county results were:
  - Jefferson received **10.5%** of the votes and **38,855** votes.
  - Denver received **82.8%** of the votes and **306,055** votes.
  - Arapahoe received **6.7%** of the votes and **24,801** votes.
    - To get the actual values, I used the following code, which combined the one from the previous step:
      ```python
      for row in election_data:
          county = row[1]
          if county not in counties:
              counties.append(county)
              county_votes[county] = 1
          else:
              county_votes[county] += 1
      ```
      - This increased the vote count by one for the county key in the dictionary if it was not already in the list.

- The county with the largest turnout was:
  - Denver with **82.8%** of the vote and **306,055** votes.
    - To calculate this, instead of using a flag and loop over the dictionary, I used the **max()** function, paired
    with a key to get the county with the largest turnout.
    ```python
    largest_county_turnout = max(county_votes, key=county_votes.get)
    ```
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received **23.0%** of the vote and **85,213** votes.
  - Diana DeGette received **73.8%** of the vote and **272,892** votes.
  - Raymon Anthony Doane received **3.1%** of the vote and **11,606** votes.
- The winner of the election was:
  - ***Diana DeGette*** with **73.8%** of the vote and **272,892** votes.

### Text File and Printed Output
- As for the text file and printed output, I initialized a string variable and called election results to store
the election data.
  - I used string concatenation to add various parts of the election data to the string that were obtained using a for
  loop such as the candidate and county names and vote counts:
    ```python
    for county in county_votes:
        county_data = f'{county}: {county_votes[county] / total_votes:.1%} ({county_votes[county]:,})\n'
        election_results += county_data
    
    for candidate in candidate_votes:
        candidate_data = f'{candidate}: {candidate_votes[candidate] / total_votes:.1%} ({candidate_votes[candidate]:,})\n'
        election_results += candidate_data
    ```
- I then used the print function to print the election results to the terminal.
- As fot the text file, instead of constantly writing to the file,  I only wrote once to it by grouping all the election
text data into a single variable:
  ```python
  with open('analysis/election_results.txt', 'w') as results_file:
      results_file.write(election_results)
  ```

## Election-Audit Summary
The election commission should consider using this script or a modified version of it to analyze the results of the
next elections, either locally or nationally. This will be quite efficient and error-proof ways to analyze the results
and share them with the public.
<br><br>
There could be various ways in which each election adapts the script to better suit its needs. The following are
suggestions in which the script can be modified for other elections:
1. Since Python capabilities and libraries are vast, the elections officials could use an API to post the results
to their official Twitter page or create a mass email (could use yagmail or SMTPEmail) with the results.
2. The CSV could contain another column with more data such as the voting time to better understand the voting patterns
that occur in each county.
3. Instead of creating a text file, the script could create a database and store the results in a database. Or it could
also store the results in a formatted Excel file using the XlsxWriter module.
4. The script could also access the data from an API or a government database instead of the CSV file. This would be
done for data safekeeping and prevent any possible modifications.

## Challenge Overview
There were several challenges that needed to be addressed for the analysis to be successful.
- A CSV had to be read in and parsed to obtain the data from the election, including the number of votes cast,
the candidates, and the votes received by each candidate and county
- A for loop was used to iterate through the data to calculate the total number of votes cast
- If statements were used to correctly add each vote to the correct candidate and county
- These data was stored in a dictionary for easy access
- The percentage of votes each candidate and county won was calculated by dividing the number of votes received by the total
- The final result summary was saved in a text file in a separate folder
