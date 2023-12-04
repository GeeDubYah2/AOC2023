import math
import unittest

INPUT = '''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

def readLines( txt ):
    lines = txt.split('\n')
    lines = [line for line in lines if 'Card' in line]
    return lines
    
def getNumbers( numberSequence ):
    numStrs = numberSequence.split()
    nums = [ int(numStr) for numStr in numStrs ]
    return nums
    
def getWinningNumbers( line ):
    winningNumsStr = line.split('|')[0].split(':')[1]
    return getNumbers( winningNumsStr )
    
def getInPlayNumbers( line ):
    inPlayNumsStr = line.split('|')[1]
    return getNumbers( inPlayNumsStr )    
    
def letsPlay( txt ):
    lines = readLines( txt )
    accumulator = 0
    for line in lines:
        winningNums    = getWinningNumbers( line )
        inPlayNums     = getInPlayNumbers( line )
        successfulNums = [num for num in inPlayNums if num in winningNums]
        score = int(math.pow( 2, len(successfulNums)-1 ))
        accumulator = accumulator + score
    return accumulator
        

class TestDay4( unittest.TestCase ):
    
    def test_readLines( self ):
        lines = readLines(INPUT)
        self.assertEqual( 6, len(lines) )
        self.assertIn('Card 1', lines[0])
        self.assertIn('Card 6', lines[-1])

    def test_getNumbers( self ):
        self.assertEqual( getNumbers('69 82 63 72 16 21 14  1 123456'), [69,82,63,72,16,21,14,1,123456] )
        self.assertEqual( getNumbers(' 69  42  '), [69,42] )
        self.assertEqual( getNumbers(''), [] )
        
    def test_getWinningNumbers( self ):
        txt = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 123456'
        self.assertEqual( getWinningNumbers( txt ), [1,21,53,59,44] )

    def test_getInPlayNumbers( self ):
        txt = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 123456'
        self.assertEqual( getInPlayNumbers( txt ), [69,82,63,72,16,21,14,1,123456] )
        
    def test_letsPlay( self ):
        txt = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        self.assertEqual( 8, letsPlay(txt) )
        
        txt = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'
        self.assertEqual( 2, letsPlay(txt) )           
        
        txt = 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'
        self.assertEqual( 0, letsPlay(txt) )
        
        self.assertEqual( 13, letsPlay(INPUT) )
        
        from dataset_day4_1 import INPUT_DAY4_1
        self.assertEqual( 28538, letsPlay(INPUT_DAY4_1) ) # <<<<< THE ANSWER IS HERE <<<<

if __name__ == '__main__':
    unittest.main()