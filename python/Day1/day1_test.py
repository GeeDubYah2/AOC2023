from   day1          import convertWordsToDigits, getValidationCodeFromLine, parseInput
from   input_data    import SMALL_EXAMPLE, INPUT_DATA
from   parameterized import parameterized
import unittest

class TestValidationCodeExtractor(unittest.TestCase):

    def test_convertWordsToDigits( self ):
        """
        Test convertWordsToDigits
        """
        self.assertEqual( '1238',       convertWordsToDigits('one2threeight')) # overlapping words
        self.assertEqual( '821',        convertWordsToDigits('eightwone'))  # overlapping words
        self.assertEqual( '18',         convertWordsToDigits('1blah8')) # characters to be ignored
        self.assertEqual( '18',         convertWordsToDigits('18')) # just digits
        self.assertEqual( '1',          convertWordsToDigits('1'))  # just one digit
        self.assertEqual( '1',          convertWordsToDigits('one')) # just one word
        self.assertEqual( '',           convertWordsToDigits('')) # empty string


    @parameterized.expand([
        True,
        False
    ] )
    def test_getValidationCodeFromLine(self, convertWords : bool) :
        """
        Run the follow with & without convertWords enabled.
        None of these examples contain convertible words so the convertWords setting won't affect the results.

        :param convertWords: boolean - is word conversion enabled?
        """
        # no digits
        self.assertEqual( 0,  getValidationCodeFromLine( '', convertWords) )
        self.assertEqual( 0,  getValidationCodeFromLine( 'abcd', convertWords) )

        # same digit for first and last.
        self.assertEqual( 11, getValidationCodeFromLine( '1', convertWords) )
        self.assertEqual( 11, getValidationCodeFromLine( '1asdfasdfasdf', convertWords) )
        self.assertEqual( 11, getValidationCodeFromLine( 'asdfas1dfasdf', convertWords) )
        self.assertEqual( 11, getValidationCodeFromLine( 'asdfasdfasdf1', convertWords) )

        # two digits.
        self.assertEqual( 14, getValidationCodeFromLine( '1__4', convertWords) )
        self.assertEqual( 14, getValidationCodeFromLine( '14', convertWords) )
        self.assertEqual( 14, getValidationCodeFromLine( '1234', convertWords) )
        self.assertEqual( 14, getValidationCodeFromLine( '1abvd4', convertWords) )

    def test_getValidationCodeFromLine_withConvertibleWords(self):
        """
        More tests for getValidationCodeFromLine. These all contain number-words.
        """
        # combos of words and digits.
        self.assertEqual(14, getValidationCodeFromLine('oneabvd4', True ))
        self.assertEqual(14, getValidationCodeFromLine('oneabvdfour', True ))
        self.assertEqual(14, getValidationCodeFromLine('onetwoabvdfour', True ))

        # one word
        self.assertEqual(99, getValidationCodeFromLine('nine', True ))

        # one word & a digit
        self.assertEqual(91, getValidationCodeFromLine('nine1', True ))

        # overlapping words
        self.assertEqual(18, getValidationCodeFromLine('oneight', True ))
        self.assertEqual(78, getValidationCodeFromLine('vjbxtseven82vxbzjdsththreeeightg', True ))
        self.assertEqual(81, getValidationCodeFromLine('eightwone', True))
        self.assertEqual(21, getValidationCodeFromLine('ightwone', True))

    @parameterized.expand([
        # tuple containing ( input-string, expectedResult_withoutWordConversion, expectedResult_withWordConversion )
        # the first batch contain no number-words
        ('',             0,  0),
        ('123\n456',     59, 59),
        ('abc\ndef',     0,  0),
        ('1abc2\n4def6', 58, 58),
        ('1abc\n2def',   33, 33),
        ('abc\n1def',    11, 11),
        ('2\ndef',       22, 22),
        (SMALL_EXAMPLE,  12+38+15+77, 12+38+15+77),

        # now some inputs that contain words.
        ('two\n1three',  11, 22+13),
        ('oneight',      0,  18),

        # the answers are here - part1 & part2.
        (INPUT_DATA,     54951, 55218)              # <<<< SOLUTION TO PART 1 and PART 2.
    ] )
    def test_parseInput( self, inputString : str, withoutWordConversion : int, withWordConversion : int ):
        """
        call parseInput twice with the same string. Once with word-conversion disabled then again with it on
        :param inputString: the input test string. can contain multiple lines ('\n' separated)
        :param withoutWordConversion: expected result with word conversion off (only process digits)
        :param withWordConversion: expected result with word conversion on (process digits and number-words).
        """
        self.assertEqual(withoutWordConversion, parseInput(inputString,False), msg='Failed withoutWordConversion on [\'%s\']'%inputString)
        self.assertEqual(withWordConversion,    parseInput(inputString, True), msg='Failed withWordConversion on [\'%s\']'%inputString)

if __name__ == '__main__':
    unittest.main()
