import unittest

from dataset import *
from day8_1_2 import *


class TestDay8 (unittest.TestCase):

    def test_readLines(self):
        self.assertIn('AAA = (BBB, CCC)', readLines(EXAMPLE_INPUT))
        self.assertEqual(8, len(readLines(EXAMPLE_INPUT)))

    def test_getDirections(self):
        self.assertEqual( 'LR', getDirections('LR') )

    def test_readNode(self):
        self.assertEqual( ('MLN', ('VGS', 'JKX')), readNode('MLN = (VGS, JKX)') )
        self.assertEqual( ('SCM', ('DPB', 'PMM')), readNode('SCM = (DPB, PMM)') )

    def test_readNodes(self):
        TEST1 = '''
        MLN = (VGS, JKX)
        SCM = (DPB, PMM)
        '''
        nodes = readNodes( readLines(TEST1) )
        self.assertIn( 'MLN', nodes )
        self.assertIn( 'SCM', nodes )
        self.assertEqual(nodes['MLN'], ('VGS', 'JKX'))
        self.assertEqual(nodes['SCM'], ('DPB', 'PMM'))

    def test_runPart1(self):
        self.assertEqual(2, runPart1( EXAMPLE_INPUT ) )
        self.assertEqual(6, runPart1( EXAMPLE_2_INPUT ))
        self.assertEqual(14681, runPart1(PUZZLE_INPUT))

        # followDirection takes in starting-locn, continues for N steps
        # returns list of locns
        # repeat for all six xxA starting points
        # zip the six locn lists
        # look for entries with 6 xxZ entries.

    @unittest.skip('skipped')
    def test_runPart2(self):
        #self.assertEqual(6, runPart2( PART2_EXAMPLE ) )
        self.assertEqual(6, runPart2( PUZZLE_INPUT ))




if __name__ == '__main__':
    unittest.main()