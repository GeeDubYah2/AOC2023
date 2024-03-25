import unittest

from dataset  import *
from solution import *


class TestDay9 (unittest.TestCase):

    def test_readLines(self):
        """ test readlines using the example input """
        self.assertIn('Time:      7  15   30', readLines(EXAMPLE_1))
        self.assertEqual(2, len(readLines(EXAMPLE_1)))

    def test_readValues(self):
        """ test readValues using the example input to read the times and distances. """
        lines = readLines(EXAMPLE_1)
        self.assertEqual( [7, 15,  30], readValues( 'Time', lines ) )
        self.assertEqual( [9, 40, 200], readValues( 'Distance', lines ) )

    def test_readRaceResults(self):
        """ test readRaceResults - returns the races results as tuples containing time & distance. """
        lines   = readLines(EXAMPLE_1)
        results = readRaceResults(lines)
        self.assertEqual( [(7,9), (15,40),  (30,200)], results )

    def test_calculateDistance( self ):
        """ test calculateDistance - test with different combinations of chargeTime and runTime. """
        self.assertEqual( calculateDistance( 1, 10 ), 10 )
        self.assertEqual( calculateDistance(2, 10), 20 )
        self.assertEqual( calculateDistance(3, 10), 30 )
        self.assertEqual( calculateDistance(4, 10), 40 )

    def test_findFasterTimes( self ):
        """ test findFasterTimes - use the example input. Check we get the values described in the description """

        """
        From the description...
        
        [Re: race 1] 4 different ways you could win: you could hold the button for 2, 3, 4, or 5 milliseconds at the 
        start of the race.

        In the second race, you could hold the button for at least 4 milliseconds and at most 11 milliseconds and beat 
        the record, a total of 8 different ways to win.

        In the third race, you could hold the button for at least 11 milliseconds and no more than 19 milliseconds and 
        still beat the record, a total of 9 ways you could win.
        """

        lines   = readLines(EXAMPLE_1)
        results = readRaceResults(lines)
        self.assertEqual( findFasterTimes( results[0] ), [2, 3, 4, 5] )
        self.assertEqual( findFasterTimes( results[1] ), [4, 5, 6, 7, 8, 9, 10, 11] )
        self.assertEqual( findFasterTimes( results[2] ), [11, 12, 13, 14, 15, 16, 17, 18, 19] )

    def test_findFasterTimes( self ):
        """ test findFasterTimes - use the example input. Check we get the values described in the description """

        """
        To see how much margin of error you have, determine the number of ways you can beat the record in each race; 
        in this example, if you multiply these values together, you get 288 (4 * 8 * 9).
        """
        lines   = readLines(EXAMPLE_1)
        results = readRaceResults(lines)

        numWaysToBeatRecord = findFasterTimesAllRaces(results)
        self.assertEqual( numWaysToBeatRecord, [4,8,9] )

    def test_findFasterTimes_2( self ):
        """ test findFasterTimes - as above but using the full PUZZLE INPUT """
        lines   = readLines(PUZZLE_INPUT_1)
        results = readRaceResults(lines)

        numWaysToBeatRecord = findFasterTimesAllRaces(results)
        self.assertEqual( numWaysToBeatRecord, [45, 19, 39, 24] )

    def test_run_part1( self ):
        """ test the run method with the part1 inputs """

        self.assertEqual( run(EXAMPLE_1), 288 )
        self.assertEqual( run(PUZZLE_INPUT_1), 800280 )   # <<<<<< ANSWER TO PART ONE

    def test_run_part2( self ):
        """ test the run method with the part2 inputs """

        self.assertEqual( run(EXAMPLE_2), 71503 )
        self.assertEqual( run(PUZZLE_INPUT_2), 45128024)   # <<<<<< ANSWER TO PART TWO


if __name__ == '__main__':
    unittest.main()
