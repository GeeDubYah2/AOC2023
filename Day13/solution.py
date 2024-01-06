import unittest

from   dataset import EXAMPLE_1, PUZZLE_INPUT
from   enum import Enum


def readLines( txt ):
    return [ l for l in txt.split('\n') if len(l) > 0 ]

def splitMirroredString( txt, idx ):
    '''
    Splits a string into to parts
    txt - string to be split
    idx - index of split. value from 1 to len(txt)-1
    returns lhs and rhs
    e.g. splitMirroredString( 'abcd dcba', 4 )
                                   ^
        --> returns 'dcba','dcba'
    '''
    lhs = ''.join(reversed(txt[:idx]))
    rhs = txt[idx:]
    return lhs, rhs

def isRowSymmetrical( stringTuple ):
    (lhs,rhs) = stringTuple
    if len(lhs) < len(rhs):
        return rhs.startswith(lhs)
    else:
        return lhs.startswith(rhs)
    return False

def findSymmetriesInRow( row, possibleSymmetries=None ):
    possibleSymmetries = list(range(1,len(row))) if not possibleSymmetries else possibleSymmetries
    foundSymms = set()
    for ps in possibleSymmetries:
        lhs,rhs = splitMirroredString( row, ps )
        if isRowSymmetrical( (lhs,rhs) ):
            foundSymms.add( ps )
    return foundSymms

def findRowSymmetries( lines ):
    possibleSymmetries = None
    for row in lines:
        possibleSymmetries = findSymmetriesInRow( row, possibleSymmetries )
        if not possibleSymmetries:
            return None
    return possibleSymmetries




