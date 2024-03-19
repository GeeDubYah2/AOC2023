
def convertWordsToDigits( line : str ) -> str:
    """ substitute words, 'one', 'two', etc. with the corresponding digit
        returns these and any other digits as a string of digits
        :param line input line (str)
        :return string containing only digits.
    """
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
    """ extract the first and last digit from line (this maybe the same character)
        convert to two digit decimal and return
    """
    if convertWords:
        line = convertWordsToDigits(line)

    # extract all digits in line
    digits=[ c for c in line if c.isdigit() ]

    # validation code is the first and last digit interpreted as a two digit decimal value
    # note: first and last characters could be the same digit. so "str1ng" would be interpreted as "11".
    validationCode=int(digits[0])*10 + int(digits[-1]) if digits else 0
    return validationCode

def parseInput( inputString : str, convertWords : bool = False ) -> int:
    """
        For each line in inputString
        Extract first and last digit (this might be the same char). Convert to two digit decimal.
        Sum up these validation codes
        :param inputString lines (one or more) to be processed
        :param convertWords : bool
            - False - only process digits.
            - True - convert number-words to digits then process
        :return the total of all validation codes.
    """
    accumulator=0
    lines = inputString.split('\n')
    for line in lines:
        # get the validation code for each line.
        # increment total in accumulator.
        accumulator = accumulator + getValidationCodeFromLine( line, convertWords )
    return accumulator
