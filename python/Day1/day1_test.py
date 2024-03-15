import unittest
from input_data import SMALL_EXAMPLE, INPUT_DATA
from parameterized import parameterized

def convertWordsToDigits( line : str ) -> str:
    ''' substitute words, 'one', 'two', etc. with the corresponding digit
        returns these and any other digits as a string of digits.
        :param line input line (str)
        :return string containing only digits.
    '''
    numbers = {
        'one'   : 1,
        'two'   : 2,
        'three' : 3,
        'four'  : 4,
        'five'  : 5,
        'six'   : 6,
        'seven' : 7,
        'eight' : 8,
        'nine'  : 9,
        'zero'  : 0,
    }
    # output: digits - string containing nothing but numerical characters.
    digits=''

    for i in range(0,len(line)):
        if line[i].isdigit():
            # we've found an actual digit. add to digits.
            digits=digits+str(line[i])
        else:
            # we've found a non-digit. check if it matches a word in "numbers".
            for num in numbers:
                if line[i:].startswith(num):
                    # found a number word. replace with digit and add to digits.
                    digits=digits+str(numbers[num])
    return digits

def getValidationCodeFromLine( line : str, convertWords : bool = False ) -> int:
    ''' extract the first and last digit from line (may be same character)
        convert to two digit decimal and return
    '''
    if convertWords:
        line = convertWordsToDigits(line)

    # extract all digits in line
    digits=[ c for c in line if c.isdigit() ]

    # validation code is the first and last digit interpreted as a two digit decimal value
    # note: first and last characters could be the same digit. so "str1ng" would be interpreted as "11".
    validationCode=int(digits[0])*10 + int(digits[-1]) if digits else 0
    return validationCode

def parseInput( inputString : str, convertWords : bool = False ) -> int:
    '''
        For each line in inputString
        Extract first and last digit (may be same char). Convert to two digit decimal.
        Sum up these validation codes
        :param inputString lines (one or more) to be processed
        :param convertWords : bool
            - False - only process digits.
            - True - convert number-words to digits then process
        :return the total of all validation codes.
    '''
    accumulator=0
    lines = inputString.split('\n')
    for line in lines:
        # get the validation code for each line.
        # increment total in accumulator.
        accumulator = accumulator + getValidationCodeFromLine( line, convertWords )
    return( accumulator )
            
class TestValidationCodeExtractor(unittest.TestCase):

    def test_convertWordsToDigits( self ):
        '''
        Test convertWordsToDigits
        '''
        self.assertEqual( '1238',       convertWordsToDigits('one2threeight')) # overlapping words
        self.assertEqual( '821',        convertWordsToDigits('eightwone'))  # overlapping words
        self.assertEqual( '18',         convertWordsToDigits('1blah8')) # characters to be ignored
        self.assertEqual( '18',         convertWordsToDigits('18')) # just digits
        self.assertEqual( '1',          convertWordsToDigits('1'))  # just one digit
        self.assertEqual( '1',          convertWordsToDigits('one')) # just one word
        self.assertEqual( '',           convertWordsToDigits('')) # empty string


    @parameterized.expand([
        (True),
        (False)
    ] )
    def test_getValidationCodeFromLine(self, convertWords : bool) :
        '''
        Run the follow with & without convertWords enabled.
        None of these examples contain convertable words so the convertWords setting won't affect the results.

        :param convertWords: boolean - is word conversion enabled?
        '''
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

    def test_getValidationCodeFromLine_withConvertableWords(self):
        '''
        Run the follow with & without convertWords enabled.
        None of these examples contain convertable words so the convertWords setting won't affect the results.

        :param convertWords: boolean - is word conversion enabled?
        '''
        '''
        Now some tests containing number-words.
        '''

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
        (INPUT_DATA,     54951, 55218)
    ] )
    def test_parseInput( self, input : str, withoutWordConversion : int, withWordConversion : int ):
        '''
        call parseInput twice with the same string. Once with word-conversion disabled then again with it on
        :param input: the input test string. can contain multiple lines ('\n' seperated)
        :param withoutWordConversion: expected result with word conversion off (only process digits)
        :param withWordConversion: expected result with word conversion on (process digits and number-words).
        '''
        self.assertEqual(withoutWordConversion, parseInput(input,False), msg='Failed withoutWordConversion on [\'%s\']'%input)
        self.assertEqual(withWordConversion,    parseInput(input, True), msg='Failed withWordConversion on [\'%s\']'%input)

if __name__ == '__main__':
    unittest.main()
