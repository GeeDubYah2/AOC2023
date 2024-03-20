import unittest

from dataset import *
from day8_1_2 import *


class TestDay8 (unittest.TestCase):

    def test_readLines(self):
        # test readlines
        self.assertIn('AAA = (BBB, CCC)', readLines(EXAMPLE_INPUT))
        self.assertEqual(8, len(readLines(EXAMPLE_INPUT)))

    def test_getDirections(self):
        # test getDirections
        self.assertEqual( 'LR', getDirections('LR') )

    def test_readNode(self):
        # test readNode with some simple examples     
        self.assertEqual( ('MLN', ('VGS', 'JKX')), readNode('MLN = (VGS, JKX)') )
        self.assertEqual( ('SCM', ('DPB', 'PMM')), readNode('SCM = (DPB, PMM)') )

    def test_readNodes(self):
        # test readNodes with some simple examples
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
        # test runPart1
        
        # using the two example inputs from the problem description
        self.assertEqual(2, runPart1( EXAMPLE_INPUT ) )
        self.assertEqual(6, runPart1( EXAMPLE_2_INPUT ))
        
        # using the full puzzle input to calculate the result.
        self.assertEqual(14681, runPart1(PUZZLE_INPUT))

if __name__ == '__main__':
    unittest.main()