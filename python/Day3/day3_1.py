import functools
import unittest

INPUT = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.587
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
    partNum  = 0
    rowIdx   = 0
    startIdx = 0
    endIdx   = 0
    
    def __init__( self, row, start ):
        self.rowIdx   = row
        self.startIdx = start
        
    def setPartNum( self, partNumStr, endIdx ):
        self.partNum = strToInt( partNumStr )
        self.endIdx  = endIdx
        
    def __str__( self ):
        retval = 'Part: %d From line: %d [%d:%d]' % ( self.partNum, self.rowIdx, self.startIdx, self.endIdx)
        return retval
    
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
    
def isLegitPart( part, lines ):
    scanStartIdx = part.startIdx-1
    scanEndIdx   = part.endIdx+1
    rowIdx       = part.rowIdx
    
    for row in range(rowIdx-1, rowIdx+2):
        #print( 'scanning: \'' + lines[row] + '\'' )
        
        for idx in range(scanStartIdx,scanEndIdx):
            c = lines[row][idx] if idx<len(lines[row]) else '.'
            #print('\'' + c + '\'')
            if not c.isalnum() and c not in ['.',' ']:
                #print( 'Found symbol: \'%s\'' % c )
                return True
    
    # no match
    return False

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
    legitParts = [ part for part in parts if isLegitPart( part, lines ) ]
    return calcPartsTotal( legitParts )
    
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
        #print(partsAsString)
        self.assertEqual( 10, len(parts) )
        self.assertIn( 'Part: 467 From line: 1 [1:4]', partsAsString )
        self.assertIn( 'Part: 598 From line: 10 [6:9]', partsAsString )
        
    def test_isLegitPart( self ):
        lines = readLines(INPUT)
        parts = findParts(lines)  

        #
        # 467..114..
        # ...*......        
        self.assertEqual( 467, parts[0].partNum ) # sanity check. 
        self.assertTrue(  isLegitPart( parts[0], lines ) ) # 467 is legit (* symbol)
        
        self.assertEqual( 114, parts[1].partNum ) # sanity check. 
        self.assertFalse( isLegitPart( parts[1], lines ) ) # 114 isn't
        
        # .....+.587  < not legit
        self.assertEqual( 587, parts[5].partNum ) # sanity check. 
        self.assertFalse( isLegitPart( parts[5], lines ) ) # 587 isn't        
        
        # ...$.*....
        # .664.598..
        # 
        self.assertEqual( 664, parts[-2].partNum ) 
        self.assertTrue(  isLegitPart( parts[-2], lines ) ) 
        
        self.assertEqual( 598, parts[-1].partNum ) 
        self.assertTrue(  isLegitPart( parts[-1], lines ) )         

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
        self.assertEqual( 4361, parseInput( INPUT ) )
        
        from dataset_3_1 import INPUT_3_1
        self.assertEqual( 519444, parseInput( INPUT_3_1 ) ) # <<<<< THE ANSWER IS HERE <<<<<

if __name__ == '__main__':
    #lines = parseInput( INPUT )
    #print( lines )
    unittest.main()
    