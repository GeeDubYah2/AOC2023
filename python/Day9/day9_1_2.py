import unittest

from   dataset import EXAMPLE_INPUT, PUZZLE_INPUT
from   enum import Enum


'''
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''

def readLines( txt ):
    return [ l for l in txt.split('\n') if len(l) > 0 ]

def strToInt( txt ):
    ''' converts txt to a decimal value. ignores everything thats not a digit
        'Game 51:' --> 51
    '''
    digits = [c for c in txt if c.isdigit() or c=='-' ]
    value  = int(''.join(digits))
    return value

def getValues( line ):
    while '  ' in line :
        line = line.replace('  ',' ')
    words = line.split(' ')
    numbers = [ strToInt(word) for word in words ]
    return numbers

def getDifferences( numbers ):
    diffs = []
    for idx in range( 0, len(numbers) ):
        if idx+1 < len(numbers):
            diffs.append( numbers[idx+1]-numbers[idx] )
    return diffs

def allZero( numbers ):
    return all( [i==0 for i in numbers] )

def calcDiffsRecursively( numbers, allDiffs ):
    diffs = getDifferences( numbers )
    if not allZero( diffs ):
        calcDiffsRecursively( diffs, allDiffs )
        allDiffs.append(diffs)
    return allDiffs

def processLine( line ):
    numbers    = getValues( line )
    allNumbers = []
    allNumbers =  calcDiffsRecursively( numbers, allNumbers )
    allNumbers.append( numbers )
    return allNumbers

def predictNextValue( allNumbers ):
    prevDiff=0
    for numList in allNumbers:
        newValue = numList[-1]+prevDiff
        numList.append(newValue)
        prevDiff = newValue
    return newValue

def predictPreviousValue( allNumbers ):
    prevDiff=0
    for numList in allNumbers:
        newValue = numList[0]-prevDiff
        numList = [newValue] + numList
        prevDiff = newValue
    return newValue

class DIRECTION(Enum):
    FORWARD  = 1
    BACKWARD = 2

    @classmethod
    def getPredictFunction( cls, direction ):
        return predictNextValue if direction==cls.FORWARD else predictPreviousValue

def run( txt, direction ):
    lines = readLines( txt )
    total = 0
    predictFunc = DIRECTION.getPredictFunction( direction )
    for line in lines:
        allNumbers = processLine( line )
        value      = predictFunc( allNumbers )
        total      = total + value
    return total

