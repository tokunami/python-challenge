import csv
import os

# function definition
def computeBudget(fileName):
    # Read though the csv of raw data
    csvpath = os.path.join('raw_data', fileName)

    # Get rownomber - 1 as totalMonths
    totalMonths = sum(1 for line in open(csvpath)) - 1

    # Assign/declaration fieleds
    totalRevenue = 0
    firstRevenue = 0
    lastRevenue = 0
    maxRevenue = 0
    minRevenue = 0
    maxMon = ''
    minMon = ''
    isFirst = False

    # Read in the csv file
    with open(csvpath, newline='') as csvfile:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip the headers
        next(csvreader, None)
        # Loop through the data
        for row in csvreader:
            # Assign firstRevenue if isFirst is False
            if not isFirst:
                firstRevenue = int(row[1])
                isFirst = True
            # Compare the values and assign if needed
            if int(row[1]) > maxRevenue:
                maxRevenue = int(row[1])
                maxMon = row[0]
            if int(row[1]) < minRevenue:
                minRevenue = int(row[1])
                minMon = row[0]
            # Sum totalRevenue
            totalRevenue = totalRevenue + int(row[1])

        # After the loop, asign lastRevenue
        lastRevenue = int(row[1])

    # compute averageRevenueChange
    avRevenueChange = int((lastRevenue - firstRevenue)/(totalMonths-1))

    print('Financial Analysis for ' + fileName)
    print('-------------------')
    print('Total Months: ' + str(totalMonths))
    print('Total Revenue: $' + str(totalRevenue))
    print('Average Revenue Change: $' + str(avRevenueChange))
    print('Greatest Invrease in Revenue: ' + maxMon + ' ($' + str(maxRevenue) + ')')
    print('Greatest Decrease in Revenue: ' + minMon + ' ($' + str(minRevenue) + ')')
    print('')

# Get all files in the directory
fileList = os.listdir('raw_data')

# Loop through files
for fileName in fileList:
    computeBudget(fileName)