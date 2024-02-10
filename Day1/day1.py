import unittest
from input_data import INPUT_DATA

def getValidationCodeFromLine( line : str ) -> int:
    ''' extract the first and last digit from line (may be same character)
        convert to two digit decimal and return
    '''
    # extract all digits in line
    digits=[ c for c in line if c.isdigit() ]

    # validation code is the first and last digit interpreted as a two digit decimal value
    # note: first and last characters could be the same digit. so "str1ng" would be interpreted as "11".
    validationCode=int(digits[0])*10 + int(digits[-1]) if digits else 0
    return validationCode

def parseInput( inputString : str ) -> int:
    ''' For each line in inputString
        Extract first and last digit (may be same char). Convert to two digit decimal.
        Sum up these validation codes
    '''
    accumulator=0
    lines = inputString.split('\n')
    for line in lines:
        # get the validation code for each line.
        # increment total in accumulator.
        accumulator=accumulator+getValidationCodeFromLine( line )
    return( accumulator )
            
class TestValidationCodeExtractor(unittest.TestCase):
    
    def test_getValidationCodeFromLine(self):
        # no digits
        self.assertEqual( 0,  getValidationCodeFromLine( '') )
        self.assertEqual( 0,  getValidationCodeFromLine( 'abcd') )

        # same digit for first and last.
        self.assertEqual( 11, getValidationCodeFromLine( '1') )
        self.assertEqual( 11, getValidationCodeFromLine( '1asdfasdfasdf') )
        self.assertEqual( 11, getValidationCodeFromLine( 'asdfas1dfasdf') )
        self.assertEqual( 11, getValidationCodeFromLine( 'asdfasdfasdf1') )

        # two digits.
        self.assertEqual( 14, getValidationCodeFromLine( '1__4') )
        self.assertEqual( 14, getValidationCodeFromLine( '14') )
        self.assertEqual( 14, getValidationCodeFromLine( '1234') )
        self.assertEqual( 14, getValidationCodeFromLine( '1abvd4') )
    
    def test_parseInput( self ):
        # one line, no digits.
        self.assertEqual( 0,     parseInput( '') )

        # two lines
        self.assertEqual( 13+46, parseInput( '123\n456') )

        # two lines - no digits.
        self.assertEqual( 0,     parseInput( 'abc\ndef') )

        # other two line combos.
        self.assertEqual( 58,    parseInput( '1abc2\n4def6') )
        self.assertEqual( 33,    parseInput( '1abc\n2def') )
        self.assertEqual( 11,    parseInput( 'abc\n1def') )
        self.assertEqual( 22,    parseInput( '2\ndef') )

        # small example input
        example = '''
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        '''
        self.assertEqual( 142,   parseInput( example ) )

        # finally the full puzzle input.
        # And the answer is....
        self.assertEqual( 54951, parseInput( INPUT_DATA ) )
    

if __name__ == '__main__':
    unittest.main()
