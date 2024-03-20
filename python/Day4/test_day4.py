import unittest
from day4  import readLines, getNumbers, getWinningNumbers, getInPlayNumbers, letsPlayPart1, getCardNumber, letsPlayPart2
from dataset import EXAMPLE_INPUT, FULL_PUZZLE_INPUT

class TestDay4( unittest.TestCase ):
    
    def test_readLines( self ):
        # test readLines with example input
        lines = readLines(EXAMPLE_INPUT)
        self.assertEqual( 6, len(lines) )
        self.assertIn('Card 1', lines[0])
        self.assertIn('Card 6', lines[-1])
        
    def test_getCardNumber( self ):
        # test getCardNumber with example input. Should return 3.
        txt = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 123456'
        self.assertEqual( getCardNumber( txt ), 3 )
        
        # test getCardNumber with extra whitespace. Should return 1234.
        txt = '      Card 1234       :  1 21 53 59 44 | 69 82 63 72 16 21 14  1 123456'
        self.assertEqual( getCardNumber( txt ), 1234 )           

    def test_getNumbers( self ):
        # test getNumbers. converts a string sequence of numbers to a list[int]...
        self.assertEqual( getNumbers('69 82 63 72 16 21 14  1 123456'), [69,82,63,72,16,21,14,1,123456] )
        self.assertEqual( getNumbers(' 69  42  '), [69,42] ) # extra white space
        self.assertEqual( getNumbers(''), [] )               # empty string
        
    def test_getWinningNumbers( self ):
        # test getWinningNumbers - returns the numbers to the left of the pipe symbol
        txt = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 123456'
        self.assertEqual( getWinningNumbers( txt ), [1,21,53,59,44] )

    def test_getInPlayNumbers( self ):
        # test getInPlayNumbers - returns the numbers to the right of the pipe symbol
        txt = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 123456'
        self.assertEqual( getInPlayNumbers( txt ), [69,82,63,72,16,21,14,1,123456] )
        
    def test_letsPlayPart1( self ):
        # call letsPlayPart1 with a simple one-line game from the example.
        txt = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        self.assertEqual( 8, letsPlayPart1(txt) )
        
        # call letsPlayPart1 with a simple one-line game from the example.
        txt = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'
        self.assertEqual( 2, letsPlayPart1(txt) )           
        
        # call letsPlayPart1 with a simple one-line game from the example.
        txt = 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'
        self.assertEqual( 0, letsPlayPart1(txt) )
        
        # call letsPlayPart1 with the full example game. Score should be 13.
        self.assertEqual( 13, letsPlayPart1(EXAMPLE_INPUT) )
        
        # finally, call letsPlayPart1 with the full puzzle input. Calculate the result.
        self.assertEqual( 28538, letsPlayPart1(FULL_PUZZLE_INPUT) ) # <<<<< PART 1 ANSWER IS HERE <<<<
        
    def test_letsPlayPart2( self ):
        # call letsPlayPart2 with a simple one-line game from the example.
        txt = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        self.assertEqual( 1, letsPlayPart2(txt) )
        
        # call letsPlayPart2 with the full example game. Score should be 30       
        self.assertEqual( 30, letsPlayPart2(EXAMPLE_INPUT) )
        
        # finally, call letsPlayPart2 with the full puzzle input. Calculate the result.
        self.assertEqual( 9425061, letsPlayPart2(FULL_PUZZLE_INPUT) ) # <<<<< PART 2 ANSWER IS HERE <<<<

if __name__ == '__main__':
    unittest.main()