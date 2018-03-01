import csv
import os
import sys
import us_state_abbrev

# function definition
def computeBudget(fileName):
    # Read though the csv of raw data
    csvpath = os.path.join('raw_data', fileName)

    # Assign/declaration fieleds
    exgHeaders = {'Emp ID':None, 'Name':None, 'DOB':None, 'SSN':None, 'State':None}
    modifiedData = []

    # Read in the csv file
    with open(csvpath, newline='') as csvfile:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Store the contents of headers and get column numbers of 'Date' and 'Revenue'
        headers = next(csvreader, None)
        for exgItem in exgHeaders:
            for index, item in enumerate(headers):
                if item == exgItem: exgHeaders[exgItem] = index
            # Exit if not above column numbers
            if exgHeaders[exgItem] is None:
                print(exgHeaders)
                sys.exit('couldn\'t calculate data. please check tha format includes "Name", "DOB", "SSN", and "State')

        print(exgHeaders)
        # Loop through the data after headers
        for row in csvreader:
            # Append modified data
            modifiedData.append([
                row[exgHeaders['Emp ID']],
                # Split Name
                row[exgHeaders['Name']].split(' ')[0],
                row[exgHeaders['Name']].split(' ')[1],
                # Change order of DOB
                row[exgHeaders['DOB']].split('-')[1] +'/' + row[exgHeaders['DOB']].split('-')[2] +'/' + row[exgHeaders['DOB']].split('-')[0],
                # Mask SSN partially
                '***-**-' + row[exgHeaders['SSN']].split('-')[2],
                # Change to abbreviation for state
                us_state_abbrev.us_state_abbrev[row[exgHeaders['State']]]
            ])

    # Write results as another csv file
    # Remove file extension from resource file
    fn = fileName[0:fileName.rfind('.')]
    with open('modified_' + fn + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])     # list（1次元配列）の場合
        writer.writerows(modifiedData)
        
# Get all files in the directory
fileList = os.listdir('raw_data')

# Loop through files
for fileName in fileList:
    computeBudget(fileName)