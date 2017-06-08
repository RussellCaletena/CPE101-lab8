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

# Define a function called lineDetails that takes in a fileName as a parameter
def lineDetails(fileName):
    fin = open(fileName)
    lineNumber = -1
    for line in fin:
        text = line
        textLength = len(text)-1
        lineNumber += 1
        print ('Line {} ({} chars): {}'.format(lineNumber, textLength, text))

# Call the lineDetails function with parameter of in.txt
lineDetails('in.txt')
