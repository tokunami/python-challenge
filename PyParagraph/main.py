import csv
import os
import re

# function definition
def computeBudget(fileName):
    # Read though the csv of raw data
    txtPath = os.path.join('raw_data', fileName)

    # Assign/declaration fieleds
    lCount = 0

    # Read paragraph
    with open(txtPath, 'r') as f:

        # Split the data on commas
        paragraph = f.read()
        sentences = re.split("(?&lt;=[.!?]) +", paragraph)
        print(sentences[1])            
        words = re.split(r'\s|\,|\.|\(|\)', paragraph)
        for word in words:
            lCount += len(word)
    
    # Generate resultstring
    resultStr = 'Paragraph Analysis for ' + fileName
    resultStr += '\n-------------------'
    resultStr += '\nApproximate Word Count: ' + str(len(words))
    resultStr += '\nApproximate Sentence Count: ' + str(len(sentences))
    resultStr += '\nAverage Letter Count: ' + str(lCount/len(words))
    resultStr += '\nAverage Sentence Length: ' + str(len(words)/len(sentences))

    # Print result
    print(resultStr + '\n')

# Get all files in the directory
fileList = os.listdir('raw_data')

# Loop through files
for fileName in fileList:
    computeBudget(fileName)