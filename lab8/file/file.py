# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

'''
Pseudocode for lineDetails:
Parameter(1): txtfile
Open and read the file
Get line number info
Get number of characters in the line
Get the text on each line
return(1): Line {} ({} chars): {}.
'''

def lineDetails(fileName):
    fin = open(fileName)
    wordsList = []
    for line in fin:
        words = line.split()
        wordsList.append(words)
    print (wordsList)

lineDetails('in.txt')
