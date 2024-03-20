import functools
import unittest
from dataset import TEST_INPUT, FULL_INPUT;


def readLines( txt ):
    """
    Parse txt and split into separate lines.
    Add spaces to start and end of each line to avoid index errors later.
    :param txt: the test input
    :return:    [ string ] containing lines
    """
    lines = []
    for line in txt.split('\n'):
        lines.append(' ' + line + ' ')
    return lines

def strToInt( txt ):
    ''' converts txt to a decimal value. ignores everything thats not a digit 
        'Game 51:' --> 51
    '''
    digits = [c for c in txt if c.isdigit() ]
    id=int(''.join(digits))
    return id    
    
class Part(object):
    """
    Represents a Part. Contains the part number, the row and start/end indexes.
    """
    partNum  = 0
    rowIdx   = 0
    startIdx = 0
    endIdx   = 0
    
    def __init__( self, row, start ):
        self.rowIdx   = row
        self.startIdx = start
        
    def setPartNum( self, partNumStr, endIdx ):
        """
        Stores details of the part number. Part number is read from a string.
        :param partNumStr:
        :param endIdx:
        """
        self.partNum = strToInt( partNumStr )
        self.endIdx  = endIdx
        
    def __str__( self ):
        """ Returns a string representation of this part """
        retval = 'Part: %d From line: %d [%d:%d]' % ( self.partNum, self.rowIdx, self.startIdx, self.endIdx)
        return retval
    
def getPart( line, rowIdx, startIdx ):
    """
    Given a row and start position - returns the Part
    :param line:        string containing the current line
    :param rowIdx:      index of the current line
    :param startIdx:    start location on this line.
    :return:            (Part, index one position after the end of this part)
    """
    p = None
    i = startIdx
    while i < len(line):
        if line[i].isdigit():
            p = Part(rowIdx, i)
            partNumStr=''            
            while line[i].isdigit():
                partNumStr=partNumStr+line[i]
                i=i+1
            p.setPartNum( partNumStr, i )
            return p,i
        else:
            i=i+1
    return p,i
    
def findParts( lines ):
    """
    Scan the lines and find all the Parts.
    :param lines: list of strings representing each line in test input
    :return:      list of all parts.
    """
    parts=[]
    for rowIdx in range( 0, len(lines) ):
        line = lines[rowIdx]
        i = 1
        while i < len(line)-1:
            if line[i].isdigit():
                part,i=getPart(line, rowIdx, i)
                parts.append(part)
            i=i+1
    return parts
    
def isLegitPart( part, lines ):
    """
    isLegitPart - Is this a valid part? i.e. is there an adjacent symbol?
    :param part:  Part to be checked.
    :param lines: list of lines
    :return:      boolean True / False
    """
    scanStartIdx = part.startIdx-1
    scanEndIdx   = part.endIdx+1
    rowIdx       = part.rowIdx
    
    for row in range(rowIdx-1, rowIdx+2):
        for idx in range(scanStartIdx,scanEndIdx):
            c = lines[row][idx] if idx<len(lines[row]) else '.'
            if not c.isalnum() and c not in ['.',' ']:
                return True
    
    # no match
    return False

def addParts( x, y ):
    """ used by reduce function to sum all part values
        will add x + y - where x & y can be a part, or integer value (sum of other parts).
    :param x: part or an integer value to be summed
    :param y: part or an integer value to be summed
    :return:  summed part values.
    """
    val1 = x if isinstance(x,int) else x.partNum
    val2 = y if isinstance(y,int) else y.partNum
    return val1 + val2

def calcPartsTotal( parts ):
    """
    Calculate the total of all part numbers.
    :param parts: list of parts
    :return:      integer sum.
    """
    if not parts:
        return 0
    elif len(parts)==1:
        return parts[0].partNum
    return functools.reduce( addParts, parts )

def parseInput( txt ):
    """
    Parse the test input. Read the lines. Find the legit parts. Total up the part numbers.
    :param txt: Test input
    :return:    The parts total (int).
    """
    lines      = readLines( txt )
    parts      = findParts( lines )
    legitParts = [ part for part in parts if isLegitPart( part, lines ) ]
    return calcPartsTotal( legitParts )


class TestDay3( unittest.TestCase ):
    
    def test_readLines(self):
        # Test the readLines function on the TEST_INPUT
        self.assertIn( ' 467..114.. ', readLines(TEST_INPUT) )
        self.assertEqual( ' 467..114.. ', readLines(TEST_INPUT)[1] )
        self.assertEqual( 12, len(readLines(TEST_INPUT)) )

    def test_strToInt(self):
        # Test the strToInt function
        # various combinations of characters (which are ignored) and digits.
        self.assertEqual( 1, strToInt('Game 1'))
        self.assertEqual( 1, strToInt('Game 1:'))
        self.assertEqual( 1, strToInt('1'))                     # digits only
        self.assertEqual( 1, strToInt('asdfasdf1asdasdasdf'))
        self.assertEqual( 1234, strToInt('G1234F_ '))
        self.assertEqual( 123, strToInt('1a2b3c '))

    def test_Part(self):
        # Test the Part constructor.
        p = Part( 1, 5 )
        self.assertEqual( 1,   p.rowIdx )
        self.assertEqual( 5,   p.startIdx )
        p.setPartNum( '123', 7 )
        self.assertEqual( 123, p.partNum )
        self.assertEqual( 7,   p.endIdx )

    def test_getPart( self ):
        # Test the getPart function. It should find two parts on this line: 467 & 114.
        line     = ' 467..114.. '
        rowIdx   = 5
        startIdx = 1
        # Get the first part 467
        p,i = getPart( line, rowIdx, startIdx )
  
        self.assertEqual( 5,   p.rowIdx )
        self.assertEqual( 1,   p.startIdx )
        self.assertEqual( 467, p.partNum )
        self.assertEqual( 4,   p.endIdx )  
        self.assertEqual( 4,   i )
        self.assertEqual( '467', line[p.startIdx:p.endIdx] )
        self.assertEqual( '.', line[i] ) # character after the part number
        self.assertEqual( 'Part: 467 From line: 5 [1:4]', str(p) )

        # Continue on to get the second part 114
        startIdx = 6
        p,i = getPart( line, rowIdx, startIdx )
  
        self.assertEqual( 5,   p.rowIdx )
        self.assertEqual( 6,   p.startIdx )
        self.assertEqual( 114, p.partNum )
        self.assertEqual( 9,   p.endIdx )  
        self.assertEqual( 9,   i )
        self.assertEqual( '114', line[p.startIdx:p.endIdx] )
        self.assertEqual( '.', line[i] ) # character after the part number      
        self.assertEqual( 'Part: 114 From line: 5 [6:9]', str(p) )

    def test_findParts( self ):
        # Call findParts on the TEST_INPUT, and check that some
        # of the expected parts are found.
        lines = readLines(TEST_INPUT)
        parts = findParts(lines)
        
        partsAsString = '\n'.join( [str(part) for part in parts] )
        self.assertEqual( 10, len(parts) )
        self.assertIn( 'Part: 467 From line: 1 [1:4]', partsAsString )
        self.assertIn( 'Part: 598 From line: 10 [6:9]', partsAsString )
        
    def test_isLegitPart( self ):
        # Call findParts on the TEST_INPUT. Check the parts that have been
        # found and test if they are legit or not. Legit means an adjacent symbol.
        lines = readLines(TEST_INPUT)
        parts = findParts(lines)  

        #
        # 467..114..
        # ...*......        
        self.assertEqual( 467, parts[0].partNum ) # sanity check. 
        self.assertTrue(  isLegitPart( parts[0], lines ) ) # 467 is legit (adjacent "*" symbol)
        
        self.assertEqual( 114, parts[1].partNum ) # sanity check. 
        self.assertFalse( isLegitPart( parts[1], lines ) ) # 114 isn't. no adjacent symbol
        
        # .....+.587  < not legit
        self.assertEqual( 587, parts[5].partNum ) # sanity check. 
        self.assertFalse( isLegitPart( parts[5], lines ) ) # 587 isn't. no adjacent symbol
        
        # ...$.*....
        # .664.598..
        # 
        self.assertEqual( 664, parts[-2].partNum ) 
        self.assertTrue(  isLegitPart( parts[-2], lines ) ) 
        
        self.assertEqual( 598, parts[-1].partNum ) 
        self.assertTrue(  isLegitPart( parts[-1], lines ) )         

    def test_calcPartsTotal( self ):
        # Test calcPartsTotal. Given a list of parts this function
        # calculates the total of all part numbers.

        # Set up some Parts.
        p1 = Part(0,0)
        p1.partNum = 111
        
        p2 = Part(0,0)
        p2.partNum = 222

        # Check the arithmetic is correct with different combos.
        self.assertEqual( 0,   calcPartsTotal( [] ) )
        self.assertEqual( 0,   calcPartsTotal( None ) )
        self.assertEqual( 111, calcPartsTotal( [p1] ) )
        self.assertEqual( 444, calcPartsTotal( [p1,p2,p1] ) )
        self.assertEqual( 333, calcPartsTotal( [p1,p2] ) )
        self.assertEqual( 222, calcPartsTotal( [p1,p1] ) )
    
    def test_parseInput( self ):
        # Test the top level function.

        # Using the test input
        self.assertEqual(   4361, parseInput( TEST_INPUT ) )

        # Using the actual input data for part one.
        self.assertEqual( 519444, parseInput( FULL_INPUT ) )    # <<<<< ANSWER TO PART ONE

if __name__ == '__main__':
    unittest.main()
    