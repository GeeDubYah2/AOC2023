import unittest

from dataset  import *
from solution import *


class TestDay9 (unittest.TestCase):

    def test_readLines(self):
        self.assertIn('Time:      7  15   30', readLines(EXAMPLE_1))
        self.assertEqual(2, len(readLines(EXAMPLE_1)))

    def test_readValues(self):
        lines = readLines(EXAMPLE_1)
        self.assertEqual( [7, 15,  30], readValues( 'Time', lines ) )
        self.assertEqual( [9, 40, 200], readValues( 'Distance', lines ) )

    def test_readRaceResults(self):
        lines   = readLines(EXAMPLE_1)
        results = readRaceResults(lines)
        self.assertEqual( [(7,9), (15,40),  (30,200)], results )

    def test_calculateDistance( self ):
        self.assertEqual( calculateDistance( 1, 10 ), 10 )
        self.assertEqual( calculateDistance(2, 10), 20 )
        self.assertEqual( calculateDistance(3, 10), 30 )
        self.assertEqual( calculateDistance(4, 10), 40 )

    def test_findFasterTimes( self ):
        lines   = readLines(EXAMPLE_1)
        results = readRaceResults(lines)
        self.assertEqual( findFasterTimes( results[0] ), [2, 3, 4, 5] )
        self.assertEqual( findFasterTimes( results[1] ), [4, 5, 6, 7, 8, 9, 10, 11] )
        self.assertEqual( findFasterTimes( results[2] ), [11, 12, 13, 14, 15, 16, 17, 18, 19] )

    def test_findFasterTimes( self ):
        lines   = readLines(EXAMPLE_1)
        results = readRaceResults(lines)

        numWaysToBeatRecord = findFasterTimesAllRaces(results)
        self.assertEqual( numWaysToBeatRecord, [4,8,9] )

    def test_findFasterTimes_2( self ):
        lines   = readLines(PUZZLE_INPUT)
        results = readRaceResults(lines)

        numWaysToBeatRecord = findFasterTimesAllRaces(results)
        self.assertEqual( numWaysToBeatRecord, [45, 19, 39, 24] )

    def test_run_part1( self ):
        self.assertEqual( run(EXAMPLE_1), 288 )
        self.assertEqual( run(PUZZLE_INPUT), 800280)

    def test_run_part2( self ):
        self.assertEqual( run(EXAMPLE_2), 71503 )
        self.assertEqual( run(PUZZLE_INPUT_2), 45128024)

if __name__ == '__main__':
    unittest.main()