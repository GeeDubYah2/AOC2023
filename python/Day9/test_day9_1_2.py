import unittest

from dataset import EXAMPLE_INPUT, PUZZLE_INPUT
from day9_1_2  import *


class TestDay9 (unittest.TestCase):

    def test_readLines(self):
        self.assertIn('0 3 6 9 12 15', readLines(EXAMPLE_INPUT))
        self.assertEqual(3, len(readLines(EXAMPLE_INPUT)))

    def test_strToInt(self):
        self.assertEqual( 1, strToInt('Game 1'))
        self.assertEqual( 1, strToInt('Game 1:'))
        self.assertEqual( 1, strToInt('1'))
        self.assertEqual( 1, strToInt('asdfasdf1asdasdasdf'))
        self.assertEqual( 1234, strToInt('G1234F_ '))
        self.assertEqual( 123, strToInt('1a2b3c '))
        self.assertEqual( -1, strToInt('-1'))
        self.assertEqual( 0, strToInt('-0'))

    def test_getValues(self):
        self.assertEqual([0, 3, 6, 9, 12, 15], getValues('0   3   6   9  12  15') )
        self.assertEqual([0, 3, 6, 9, 12, 15], getValues('0 3 6 9 12 15') )

    def test_getDifferences(self):
        self.assertEqual( [3, 3, 3, 3, 3], getDifferences([0, 3, 6, 9, 12, 15]) )
        self.assertEqual( [0, 0 ,0 ,0], getDifferences([3, 3, 3, 3, 3]))

    def test_allZero( self ):
        self.assertTrue( allZero( [0, 0 ,0 ,0] ) )
        self.assertTrue( allZero( [0] ) )
        self.assertFalse(allZero( [1] ) )
        self.assertFalse(allZero( [0,0,0,0,0,0,0,0,0,1] ) )

    def test_calcDiffsRecursively(self):
        allDiffs = calcDiffsRecursively( [0, 3, 6, 9, 12, 15], [] )
        self.assertEqual( allDiffs, [[3, 3, 3, 3, 3]] )

        allDiffs = calcDiffsRecursively( [10,13,16,21,30,45,68], [] )
        self.assertEqual( allDiffs, [[2, 2, 2, 2], [0, 2, 4, 6, 8], [3, 3, 5, 9, 15, 23]] )

    def test_processLine(self):
        allNumbers = processLine( '0   3   6   9  12  15' )
        self.assertEqual( allNumbers, [[3, 3, 3, 3, 3], [0, 3, 6, 9, 12, 15]] )
        self.assertEqual( 18, predictNextValue( allNumbers ) )
        self.assertEqual( -3,  predictPreviousValue(allNumbers) )

        allNumbers = processLine( '1 3 6 10 15 21' )
        self.assertEqual( allNumbers, [[1, 1, 1, 1], [2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21]] )
        self.assertEqual( 28, predictNextValue( allNumbers ) )
        self.assertEqual( 0,  predictPreviousValue(allNumbers) )

        allNumbers = processLine( '10  13  16  21  30  45' )
        self.assertEqual( allNumbers, [[2, 2, 2],[0, 2, 4, 6],[3, 3, 5, 9, 15],[10,13,16,21,30,45]] )
        self.assertEqual( 68, predictNextValue(allNumbers))
        self.assertEqual( 5,  predictPreviousValue(allNumbers) )

    def test_run( self ):
        # PART 1 - predict forward
        self.assertEqual( 114, run(EXAMPLE_INPUT, DIRECTION.FORWARD) )
        self.assertEqual(1995001648, run(PUZZLE_INPUT, DIRECTION.FORWARD))  # <<< THE ANSWER <<<

        # PART 2 - predict backward
        self.assertEqual(2, run(EXAMPLE_INPUT, DIRECTION.BACKWARD))
        self.assertEqual(988, run(PUZZLE_INPUT, DIRECTION.BACKWARD))  # <<< THE ANSWER <<<

if __name__ == '__main__':
    unittest.main()