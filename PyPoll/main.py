import csv
import os
import sys

# function definition
def computeBudget(fileName):
    # Read though the csv of raw data
    csvpath = os.path.join('raw_data', fileName)

    # Get rownumber - 1 as totalVotes
    totalVotes = sum(1 for line in open(csvpath)) - 1

    # Assign/declaration fieleds
    candidates = {}

    # Read in the csv file
    with open(csvpath, newline='') as csvfile:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Store the contents of headers and get column numbers of 'Date' and 'Revenue'
        headers = next(csvreader, None)
        for index, item in enumerate(headers):
            if item == 'Candidate': candCol = index
        
        # Exit if not above column numbers
        if not 'candCol' in locals():
            sys.exit('couldn\'t calculate data. please check tha format includes "Candidate"')

        # Loop through the data after headers
        for row in csvreader:
            # Add a candidate to the list if it doesn't exist
            if not row[candCol] in candidates:
                candidates[row[candCol]] = 1
            # Count up if it exists
            else:
                candidates[row[candCol]] += 1

    # Generate resultstring
    resultStr = 'Election Results for ' + fileName
    resultStr += '\n---------------------------'
    resultStr += '\nTotal Votes: ' + str(totalVotes)
    resultStr += '\n---------------------------'
    for candidate, votes in candidates.items():
        resultStr += '\n' + candidate + ': {:.1%}'.format(votes/totalVotes) + ' (' + str(votes) + ')'
    resultStr += '\n---------------------------'
    resultStr += '\nWinner: ' + str(max(candidates.items(), key=lambda x:x[1])[0])
    resultStr += '\n---------------------------'

    # Print result
    print(resultStr + '\n')

    # Write results as a text file
    # Remove file extension from resource file
    fn = fileName[0:fileName.rfind('.')]
    writeFile = open('result_' + fn + '.txt','w')
    writeFile.write(resultStr)

# Get all files in the directory
fileList = os.listdir('raw_data')

# Loop through files
for fileName in fileList:
    computeBudget(fileName)