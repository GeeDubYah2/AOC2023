import unittest

from dataset import *
from day8 import *


class TestDay8 (unittest.TestCase):

    def test_readLines(self):
        """ test readlines """
        self.assertIn('AAA = (BBB, CCC)', readLines(PART1A_EXAMPLE))
        self.assertEqual(8, len(readLines(PART1A_EXAMPLE)))

    def test_getDirections(self):
        """ test getDirections """
        self.assertEqual( 'LR', getDirections('LR') )

    def test_readNode(self):
        """ test readNode with some simple examples  """    
        self.assertEqual( ('MLN', ('VGS', 'JKX')), readNode('MLN = (VGS, JKX)') )
        self.assertEqual( ('SCM', ('DPB', 'PMM')), readNode('SCM = (DPB, PMM)') )

    def test_readNodes(self):
        """ test readNodes with some simple examples """ 
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
        """ test runPart1 with the examples from the AOC page and the full puzzle input """
        
        # using the two example inputs from the problem description
        self.assertEqual(2, runPart1( PART1A_EXAMPLE ) )
        self.assertEqual(6, runPart1( PART1B_EXAMPLE ))
        
        # using the full puzzle input to calculate the result.
        self.assertEqual(14681, runPart1(PUZZLE_INPUT))                      # <<<<<<< ANSWER TO PART 1 <<<<<<<

    def test_runPart2(self):
        """ test runPart2 with the example from the AOC page and the full puzzle input """
        self.assertEqual( 6, runPart2( PART2_EXAMPLE, 100 ) )
        self.assertEqual( 14321394058031, runPart2( PUZZLE_INPUT, 100000 ) ) # <<<<<<< ANSWER TO PART 2 <<<<<<<

if __name__ == '__main__':
    unittest.main()