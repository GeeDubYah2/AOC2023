import functools
import unittest
from   dataset   import TEST_INPUT, FULL_INPUT


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
    """ converts txt to a decimal value. ignores everything thats not a digit
        'Game 51:' --> 51
    """
    digits = [c for c in txt if c.isdigit() ]
    value=int(''.join(digits))
    return value
    
class Part(object):
    """
    Represents a Part. Contains the part number, the row and start/end indexes.
    """
    def __init__( self, row, start ):
        self.partNum   = 0
        self.rowIdx    = row
        self.startIdx  = start
        self.endIdx    = 0
        self.gearLocns = []
        
    def setPartNum( self, partNumStr, endIdx ):
        """
        Stores details of the part number. Part number is read from a string.
        :param partNumStr:
        :param endIdx:
        """
        self.partNum = strToInt( partNumStr )
        self.endIdx  = endIdx
        
    def addGearLocn( self, row, idx ):
        """ Add the location of an adjacent gear symbol ("*").
        """
        self.gearLocns.append( (row,idx) )
        
    def __str__( self ):
        """ Returns a string representation of this part """
        retval = 'Part: %d From line: %d [%d:%d]' % ( self.partNum, self.rowIdx, self.startIdx, self.endIdx)
        return retval
        
class Gear(object):
    def __init__( self, locn ):
        """ locn - tuple containing (rowIdx,colIdx) """
        self.locn  = locn
        self.parts = []
        
    def addPart( self, part ):
        """ Add a part to this gear.
        """
        self.parts.append( part )
        
    
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
    
def isGearComponent( part, lines, gears ):
    """
    isLegitPart - Is this Part a component in a gear? To be a gear it must be adjacent to a "*" that is
                  adjacent to another Part. If it is a gear component append the Gear to "gears".
    :param part:  Part to be checked.
    :param lines: list of lines
    :param gears: list of gears - updated in place
    :return:      boolean True / False
    """
    scanStartIdx = part.startIdx-1
    scanEndIdx   = part.endIdx+1
    rowIdx       = part.rowIdx

    # Check one row above & below; and one column left & right of this part.
    for row in range(rowIdx-1, rowIdx+2):
        for idx in range(scanStartIdx,scanEndIdx):

            # Search for gear symobls - "*".
            c = lines[row][idx] if idx<len(lines[row]) else '.'
            if c == '*':
                # Add Gear to Part
                part.addGearLocn(row,idx)

                # Add the new Gear to "gears" if not there already.
                if (row,idx) in gears:
                    gear = gears[(row,idx)]
                else:
                    gear = Gear((row,idx))
                    gears[(row,idx)] = gear
                gear.addPart( part )

    return bool(part.gearLocns)

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

def parseInput( txt ):
    """
    Parse the test input. Read the lines. Find parts that are components in a gear. Then
    calculate the total gear ratio for all gears.

    :param txt: Test input
    :return:    The total gear ratio.
    """
    lines      = readLines( txt )
    parts      = findParts( lines )
    gears      = {} # dictionary of (rowIdx,colIdx):Gear
    
    for part in parts:
        isGearComponent( part, lines, gears )

    # Calculate the total gear ratio for all gears containing two parts.
    accumulator = 0
    for g in gears:

        # Does the gear have two parts?
        if len( gears[g].parts ) == 2:

            # Yes, gear ratio is part1 * part2.
            accumulator = accumulator + gears[g].parts[0].partNum * gears[g].parts[1].partNum
    
    return accumulator



#######################################################################################################
#######################################################################################################

    
class TestDay3( unittest.TestCase ):
    
    def test_readLines(self):
        # Test the readLines function on the TEST_INPUT
        self.assertIn( ' 467..114.. ', readLines(TEST_INPUT))
        self.assertEqual( ' 467..114.. ', readLines(TEST_INPUT)[1])
        self.assertEqual(12, len(readLines(TEST_INPUT)))

    def test_strToInt(self):
        # Test the strToInt function
        # various combinations of characters (which are ignored) and digits.
        self.assertEqual( 1, strToInt('Game 1'))
        self.assertEqual( 1, strToInt('Game 1:'))
        self.assertEqual( 1, strToInt('1'))
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
        
    def test_isGearComponent( self ):
        # Test isGearComponent. A gear is two parts separated by a "*".
        lines = readLines(TEST_INPUT)
        parts = findParts(lines)  
        gears = {}
        
        self.assertEqual( 10, len(parts) )         

        #
        # 467..114..
        # ...*......        
        self.assertEqual( 467, parts[0].partNum ) # is a gear component
        self.assertTrue(  isGearComponent( parts[0], lines, gears ) ) 
        
        self.assertEqual( 114, parts[1].partNum ) # is not a gear component
        print( parts[1].gearLocns )
        self.assertFalse( isGearComponent( parts[1], lines, gears ) ) 
        
        # 617*......
        self.assertEqual( 617, parts[4].partNum ) # is a gear component. but not a pair. 
        self.assertTrue(  isGearComponent( parts[4], lines, gears ) )         
        
        # ...$.*....
        # .664.598..
        # 
        self.assertEqual( 664, parts[-2].partNum ) # is not a gear component
        self.assertFalse( isGearComponent( parts[-2], lines, gears ) ) 
        
        self.assertEqual( 598, parts[-1].partNum ) # is a gear component
        self.assertTrue(  isGearComponent( parts[-1], lines, gears ) )        
        
    def test_isGearComponent_test2( self ):

        # Small test input. Contains one gear consisting of parts 123 and 456.
        SMALL_TEST_INPUT = """
..123....
.*...*...
......456
.........
"""
        lines = readLines(SMALL_TEST_INPUT)
        parts = findParts(lines) 
        gears = {}
        self.assertEqual( 2, len(parts) ) 
        
        self.assertEqual( 123, parts[0].partNum ) # is a gear component
        self.assertTrue(  isGearComponent( parts[0], lines, gears ) ) 
        self.assertEqual( 2, len(parts[0].gearLocns) )
        self.assertEqual( [(2,2),(2,6)], parts[0].gearLocns )
        
        self.assertEqual( 456, parts[1].partNum ) # is a gear component
        self.assertTrue(  isGearComponent( parts[1], lines, gears ) )         
        self.assertEqual( 1, len(parts[1].gearLocns) )
        self.assertEqual( [(2,6)], parts[1].gearLocns )
        
    def test_isGearComponent_test3( self ):
        SMALL_TEST_INPUT = """
..123.56.
.....*...
......456
...22*..*
"""
        lines = readLines(SMALL_TEST_INPUT)
        parts = findParts(lines)  
        
        self.assertEqual( 4, len(parts) ) 
        
        gears = {}

        part=parts[0]
        self.assertEqual( 123, part.partNum ) # is a gear component
        self.assertTrue(  isGearComponent( part, lines, gears ) ) # updates gears for all gears on part
        self.assertEqual( 1, len(part.gearLocns) )
        self.assertEqual( [(2,6)], part.gearLocns )

        # check the gear at 2,6 has been added to gears and references back to parts[0]
        self.assertIn( (2,6), gears )
        self.assertEqual( 1, len(gears[(2,6)].parts) )
        self.assertEqual( part, gears[(2,6)].parts[0] )
        
        part=parts[2]
        self.assertEqual( 456, part.partNum ) # is a gear component
        self.assertTrue(  isGearComponent( part, lines, gears ) ) # updates gears for all gears on part      
        self.assertEqual( 3, len(part.gearLocns) )
        self.assertEqual( [(2,6),(4,6),(4,9)], part.gearLocns )      

        # check the gear at 2,6 has been updated with the new part - parts[1]
        self.assertEqual( 2, len(gears[(2,6)].parts) )
        self.assertEqual( parts[0], gears[(2,6)].parts[0] )
        self.assertEqual( parts[2], gears[(2,6)].parts[1] )

        # the follow gears should have been added too.
        self.assertIn( (4,6), gears )
        self.assertIn( (4,9), gears )
        
        # note: parts[1] "56" isn't included as we haven't called isGearComponent on it
        # likewise parts[3] "22"
    
    def test_parseInput( self ):
        # Test the top level function.

        # Small example containing two parts 456 and 22.
        SMALL_TEST_INPUT = """
        ..123.56.
        .....*...
        ......456
        ...22*..*
        """
        self.assertEqual( 456*22, parseInput( SMALL_TEST_INPUT ) )

        # Using the test input
        self.assertEqual(467835, parseInput(TEST_INPUT))
        # Using the actual input data for part two.
        self.assertEqual(74528807, parseInput(FULL_INPUT)) # <<<<< THE ANSWER IS HERE <<<<<

if __name__ == '__main__':
    unittest.main()
