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
        #TODO judge the contents of headers
        next(csvreader, None)
        # Loop through the data
        for row in csvreader:
            # Assign firstRevenue if isFirst is False
            if not isFirst:
                firstRevenue = int(row[1])
                isFirst = True
            # Compare the values and assign max/min if needed
            if int(row[1]) > maxRevenue:
                maxRevenue = int(row[1])
                maxMon = row[0]
            if int(row[1]) < minRevenue:
                minRevenue = int(row[1])
                minMon = row[0]
            # Sum totalRevenue
            totalRevenue = totalRevenue + int(row[1])

        # After the loop, assign lastRevenue
        lastRevenue = int(row[1])

    # Compute averageRevenueChange
    avRevenueChange = int((lastRevenue - firstRevenue)/(totalMonths-1))

    # Generate resultstring
    resultStr = 'Financial Analysis for ' + fileName
    resultStr += '\n-------------------'
    resultStr += '\nTotal Months: ' + str(totalMonths)
    resultStr += '\nTotal Revenue: $' + str(totalRevenue)
    resultStr += '\nAverage Revenue Change: $' + str(avRevenueChange)
    resultStr += '\nGreatest Invrease in Revenue: ' + maxMon + ' ($' + str(maxRevenue) + ')'
    resultStr += '\nGreatest Decrease in Revenue: ' + minMon + ' ($' + str(minRevenue) + ')'

    # Print result
    print(resultStr + '\n')

    # Write results as a text file
    # Remove file extension
    fn = fileName[0:fileName.rfind('.')]
    writeFile = open('analysis_' + fn + '.txt','w')
    writeFile.write(resultStr)

# Get all files in the directory
fileList = os.listdir('raw_data')

# Loop through files
for fileName in fileList:
    computeBudget(fileName)