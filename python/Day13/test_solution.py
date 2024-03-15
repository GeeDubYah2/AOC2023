import unittest

from dataset  import *
from solution import *


class TestDay9 (unittest.TestCase):

    def test_readLines(self):
        self.assertIn('#.##..##.', readLines(EXAMPLE_1))
        self.assertEqual(7, len(readLines(EXAMPLE_1)))

    def test_splitMirroredString( self ):
        self.assertEqual(('dcba', 'dcba'),  splitMirroredString('abcddcba', 4) )
        self.assertEqual(('cba', 'ddcba'), splitMirroredString('abcddcba', 3))
        self.assertEqual(('a', 'bcddcba'), splitMirroredString('abcddcba', 1))
        self.assertEqual(('bcddcba', 'a'), splitMirroredString('abcddcba', 7))

    def test_isRowSymmetrical( self ):
        self.assertTrue(  isRowSymmetrical( splitMirroredString('abcddcba', 4) ) )
        self.assertFalse( isRowSymmetrical( splitMirroredString('abcddcba', 1) ) )
        self.assertFalse( isRowSymmetrical( splitMirroredString('abcddcba', 7) ) )

    def test_findSymmetriesInRow( self ):
        self.assertEqual( {4},     findSymmetriesInRow( 'abcddcba', None ) )
        self.assertEqual( {1,4,7}, findSymmetriesInRow( 'aabccbaa', None ) )
        self.assertEqual( {1},     findSymmetriesInRow( 'aabccbaa', {1}) )
        self.assertEqual( set(),   findSymmetriesInRow( 'aabccbaa', {5}) )

    def test_findSymmetriesInRow( self ):
        self.assertEqual( {5},  findRowSymmetries( readLines(EXAMPLE_1) ) )
        self.assertEqual( None, findRowSymmetries( readLines(EXAMPLE_2) ) )

if __name__ == '__main__':
    unittest.main()