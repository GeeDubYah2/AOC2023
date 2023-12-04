import functools
import unittest

INPUT = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

def readLines( txt ):
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

    def __init__( self, row, start ):
        self.partNum   = 0
        self.rowIdx    = row
        self.startIdx  = start
        self.endIdx    = 0
        self.gearLocns = []
        
    def setPartNum( self, partNumStr, endIdx ):
        self.partNum = strToInt( partNumStr )
        self.endIdx  = endIdx
        
    def addGearLocn( self, row, idx ):
        self.gearLocns.append( (row,idx) )
        
    def __str__( self ):
        retval = 'Part: %d From line: %d [%d:%d]' % ( self.partNum, self.rowIdx, self.startIdx, self.endIdx)
        return retval
        
class Gear(object):
    def __init__( self, locn ):
        ''' locn - tuple containing rowIdx,colIdx '''
        self.locn  = locn
        self.parts = []
        
    def addPart( self, p ):
        self.parts.append( p )
        
    
def getPart( line, rowIdx, startIdx ):
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
    scanStartIdx = part.startIdx-1
    scanEndIdx   = part.endIdx+1
    rowIdx       = part.rowIdx
    
    for row in range(rowIdx-1, rowIdx+2):
        for idx in range(scanStartIdx,scanEndIdx):
            c = lines[row][idx] if idx<len(lines[row]) else '.'
            if c == '*':
                part.addGearLocn(row,idx)
                if (row,idx) in gears:
                    gear = gears[(row,idx)]
                else:
                    gear = Gear((row,idx))
                    gears[(row,idx)] = gear
                gear.addPart( part )

    return bool(part.gearLocns)

def addParts( x, y ):
    val1 = x if isinstance(x,int) else x.partNum
    val2 = y if isinstance(y,int) else y.partNum
    return val1 + val2

def calcPartsTotal( parts ):
    if not parts:
        return 0
    elif len(parts)==1:
        return parts[0].partNum
    return functools.reduce( addParts, parts )

def parseInput( txt ):
    lines      = readLines( txt )
    parts      = findParts( lines )
    gears      = {} # dictionary of (rowIdx,colIdx):Gear
    
    for part in parts:
        isGearComponent( part, lines, gears )
    
    accumulator = 0
    for g in gears:
        if len( gears[g].parts ) == 2:          
            accumulator = accumulator + gears[g].parts[0].partNum * gears[g].parts[1].partNum
    
    return accumulator



#######################################################################################################
#######################################################################################################

    
class TestDay3( unittest.TestCase ):
    
    def test_readLines(self):
        self.assertIn( ' 467..114.. ', readLines(INPUT) )
        self.assertEqual( ' 467..114.. ', readLines(INPUT)[1] )
        self.assertEqual( 12, len(readLines(INPUT)) )

    def test_strToInt(self):
        self.assertEqual( 1, strToInt('Game 1'))
        self.assertEqual( 1, strToInt('Game 1:'))
        self.assertEqual( 1, strToInt('1'))
        self.assertEqual( 1, strToInt('asdfasdf1asdasdasdf'))
        self.assertEqual( 1234, strToInt('G1234F_ '))
        self.assertEqual( 123, strToInt('1a2b3c '))
        
    def test_Part(self):
        p = Part( 1, 5 )
        self.assertEqual( 1,   p.rowIdx )
        self.assertEqual( 5,   p.startIdx )
        p.setPartNum( '123', 7 )
        self.assertEqual( 123, p.partNum )
        self.assertEqual( 7,   p.endIdx )
        
    def test_getPart( self ):
        # def getPart( line, rowIdx, startIdx ):
        line     = ' 467..114.. '
        rowIdx   = 5
        startIdx = 1
        p,i = getPart( line, rowIdx, startIdx )
  
        self.assertEqual( 5,   p.rowIdx )
        self.assertEqual( 1,   p.startIdx )
        self.assertEqual( 467, p.partNum )
        self.assertEqual( 4,   p.endIdx )  
        self.assertEqual( 4,   i )
        self.assertEqual( '467', line[p.startIdx:p.endIdx] )
        self.assertEqual( '.', line[i] ) # character after the part number
        self.assertEqual( 'Part: 467 From line: 5 [1:4]', str(p) )
        
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
        lines = readLines(INPUT)
        parts = findParts(lines)
        
        partsAsString = '\n'.join( [str(part) for part in parts] )
        self.assertEqual( 10, len(parts) )
        self.assertIn( 'Part: 467 From line: 1 [1:4]', partsAsString )
        self.assertIn( 'Part: 598 From line: 10 [6:9]', partsAsString )
        
    def test_isGearComponent( self ):
        lines = readLines(INPUT)
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
        TEST_INPUT = '''
..123....
.*...*...
......456
.........
'''
        lines = readLines(TEST_INPUT)
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
        TEST_INPUT = '''
..123.56.
.....*...
......456
...22*..*
'''
        lines = readLines(TEST_INPUT)
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
        
        # note: parts[1] "56" isnt included as we havent called isGearComponent on it
        # likewise parts[3] "22"

        

    def test_calcPartsTotal( self ):
        p1 = Part(0,0)
        p1.partNum = 111
        
        p2 = Part(0,0)
        p2.partNum = 222
        
        self.assertEqual( 0,   calcPartsTotal( [] ) )
        self.assertEqual( 0,   calcPartsTotal( None ) )
        self.assertEqual( 111, calcPartsTotal( [p1] ) )
        self.assertEqual( 444, calcPartsTotal( [p1,p2,p1] ) )
        self.assertEqual( 333, calcPartsTotal( [p1,p2] ) )
        self.assertEqual( 222, calcPartsTotal( [p1,p1] ) )
    
    def test_parseInput( self ):
        TEST_INPUT = '''
..123.56.
.....*...
......456
...22*..*
'''
        self.assertEqual( 456*22, parseInput( TEST_INPUT ) )
        
        self.assertEqual( 467835, parseInput( INPUT ) )
        
        from dataset_3_1 import INPUT_3_1
        self.assertEqual( 74528807, parseInput( INPUT_3_1 ) ) # <<<<< THE ANSWER IS HERE <<<<<

if __name__ == '__main__':

    unittest.main()
    
