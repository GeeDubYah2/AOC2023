import unittest
from dataset import MAIN_DATASET


def strToInt( txt ):
    """ converts txt to a decimal value. ignores everything that's not a digit 
        'Game 51:' --> 51
    """
    digits = [c for c in txt if c.isdigit() ]
    value=int(''.join(digits))
    return value    
    
def getColour( txt ):
    """ returns one of red, green, blue from txt """
    COLOURS = ['red','green','blue']
    for c in COLOURS:
        if c in txt:
            return c

def parseGameId( gameIdStr ):
    """ parses the game id at the start of each line. """
    return strToInt(gameIdStr)

def parseGameResults( resultsStr ):
    """  ' 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green' --> 
        returns the maximum number of each colour in each handful
        in this case {'red':4, 'green':2, 'blue':6) """
    rgbMaximums={
        'red'   : 0,
        'green' : 0,
        'blue'  : 0,
        }
        
    handfuls=resultsStr.split(';')    
    for handful in handfuls:
        """ e.g. 3 blue, 4 red """
        colourCounts=handful.split(',')
        for c in colourCounts:
            """ e.g. 3 blue """
            count  = strToInt(c)
            colour = getColour(c)
            rgbMaximums[colour]=max(rgbMaximums[colour],count)
    return rgbMaximums

def isGameValid( rgbMaximums ):
    """ returns game id if game's max cube count is less than or equal to the maximums for each colour """
    return rgbMaximums['red'] <= 12 and rgbMaximums['green'] <= 13 and rgbMaximums['blue'] <= 14

def parseGameResultsLine( line ):
    """
    :param line: parses the game results line - e.g. "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    :return: game ID
    """
    if line and 'Game' in line:
        gameIDStr   = line.split(':')[0]
        gameId      = parseGameId(gameIDStr)
        
        resultsStr  = line.split(':')[-1]        
        rgbMaximums = parseGameResults(resultsStr)
        
        if isGameValid( rgbMaximums ):
            return gameId
    return 0

def parseGameData( data ):
    """
    :param data: Processes the entire game results data. Multiple lines
    :return: the puzzle answer.
    """
    accumulator=0
    for line in data.split('\n'):
        gameIdValid = parseGameResultsLine( line )
        accumulator = accumulator + gameIdValid
    return accumulator



class TestGameResults( unittest.TestCase ):
    
    def test_strToInt(self):
        """
        tests the strToInt function with different combinations of characters(ignored) and digits.
        """
        self.assertEqual( 1,    strToInt('Game 1'))
        self.assertEqual( 1,    strToInt('Game 1:'))
        self.assertEqual( 1,    strToInt('1'))
        self.assertEqual( 1,    strToInt('asdfasdf1asdasdasdf'))
        self.assertEqual( 1234, strToInt('G1234F_ '))
        self.assertEqual( 123,  strToInt('1a2b3c '))

    def test_parseGameId(self):
        self.assertEqual( 1,    parseGameId('Game 1'))
        self.assertEqual( 1,    parseGameId('Game 1:'))
        self.assertEqual( 1,    parseGameId('1'))
        self.assertEqual( 1,    parseGameId('asdfasdf1asdasdasdf'))
        self.assertEqual( 1234, parseGameId('G1234F_ '))
        
    def test_getColour(self):
        self.assertEqual( 'red',   getColour('asdfsdfredasdfasdfsd') )
        self.assertEqual( 'blue',  getColour('blue') )
        self.assertEqual( 'green', getColour('1234 green 5678') )
        self.assertEqual( None,    getColour('') )
        
    def test_parseGameResults(self):
        self.assertEqual( {'red':1,  'green':0,  'blue':0}, parseGameResults(' 1 red') )
        self.assertEqual( {'red':0,  'green':1,  'blue':0}, parseGameResults(' 1 green') )
        self.assertEqual( {'red':0,  'green':0,  'blue':1}, parseGameResults(' 1 blue') )
        self.assertEqual( {'red':4,  'green':2,  'blue':6}, parseGameResults(' 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') )
        self.assertEqual( {'red':20, 'green':13, 'blue':6}, parseGameResults(' 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') )
    
    def test_isGameValid( self ):
        self.assertTrue(  isGameValid( {'red':1,  'green':2,  'blue':3} ) )     # within limits
        self.assertTrue(  isGameValid( {'red':12, 'green':13, 'blue':14} ) )    # equal to limits
        self.assertFalse( isGameValid( {'red':13, 'green':14, 'blue':15} ) )    # just outside limits
        self.assertFalse( isGameValid( {'red':13, 'green':1,  'blue':3} ) )     # red too high
        self.assertFalse( isGameValid( {'red':1,  'green':14, 'blue':3} ) )     # green too high
        self.assertFalse( isGameValid( {'red':1,  'green':2,  'blue':15} ) )    # blue too high
        self.assertTrue(  isGameValid( {'red':0,  'green':0,  'blue':0} ) )     # within limits
        
    def test_parseGameResultsLine(self):
        self.assertEqual( 2, parseGameResultsLine('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') )         # within limits
        self.assertEqual( 0, parseGameResultsLine('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') ) # red is too high
        self.assertEqual( 0, parseGameResultsLine('') )
        self.assertEqual( 0, parseGameResultsLine('asdfasdfasdf') )
        self.assertEqual( 0, parseGameResultsLine('Game 12: 99 red') )
        self.assertEqual( 13, parseGameResultsLine('Game 13: 1 red') )

    def test_parseGameData(self):
        DATA0 = """
        Game 13: 1 red
        """
        self.assertEqual( 13, parseGameData( DATA0 ) )
        
        DATA1 = """
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        """
        self.assertEqual( 2, parseGameData( DATA1 ) )
        
        DATA2 = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """
        self.assertEqual( 8, parseGameData( DATA2 ) )        
        
        self.assertEqual( 2149, parseGameData( MAIN_DATASET ) )  # <<<<<< PART1 solution.


if __name__ == '__main__':
    unittest.main()


