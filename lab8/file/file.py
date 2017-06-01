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
        #words = line.split()
        #wordsList.append(words)
        text = line
        #print (len(fin.readlines()))
        #a = fin.readline()
        #b = fin.readline()
        #print (a)
        #print (len(a)-1)
        #print (b)
        #print (len(b)-1)
        #print (wordsList)
        print ('Line 0 (0 chars): {}'.format(text))

lineDetails('in.txt')
