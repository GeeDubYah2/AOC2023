# AOC2023 Day 4 - https://adventofcode.com/2023/day/4
# 
# Scratchcards - Part 1:
#
#   Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#   Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
#
#  - Parse the input. 
#  - Each line has winning numbers on the left, "|", then the in-play numbers.
#  - Count how many in-play numbers match the winning numbers on that line.
#  - Score 1 point for one winning card then double for each subsequent winning card on that line.
#  - Add up the total score.
#
#
#  Scratchcards - Part 2:
#
#  - Parse the input. 
#  - Each line has winning numbers on the left, "|", then the in-play numbers.
#  - Count how many in-play numbers match the winning numbers on that line.
#  - Instead of points - each winning number gets you an extra copy of one of the next cards.
#  -   - e.g. scoring 5 points on card 10 would get you one extra copy of 11, 12, 13, 14, and 15
#  - copies score the same as originals. if you have 5 copies of card 10 - the 5 points would buy 5-copies x 5-points = 25 extra cards
#  - total up the number of scratchcards.
import math
import unittest

def readLines( txt : str ) -> list[str] :
    """Read txt line by line and return as a list[str]
    """
    lines = txt.split('\n')
    lines = [line for line in lines if 'Card' in line]
    return lines
    
def getNumbers( numberSequence : str ) -> list[int]:
    """ Reads a space delimited list of numbers and returns it as an [int]
    """
    numStrs = numberSequence.split()
    return [ int(numStr) for numStr in numStrs ]

def strToInt( txt : str ) -> int:
    """ converts txt to a decimal value. ignores everything thats not a digit 
        'Game 51:' --> 51
    """
    digits = [c for c in txt if c.isdigit() ]
    return int(''.join(digits))    

def getCardNumber( line : str ) -> int:
    """ gets the card number from the start of the line ("Card %d:")
    """
    txt = line.split(':')[0]
    return strToInt( txt )
    
def getWinningNumbers( line : str ) -> list[int]:
    """ Reads the numbers from the left hand side of line (before the "|")
    :return list[int]: list of winning numbers
    """
    winningNumsStr = line.split('|')[0].split(':')[1]
    return getNumbers( winningNumsStr )
    
def getInPlayNumbers( line : str ) -> list[int]:
    """ Reads the numbers from the right hand side of line ( after the "|")
    :return list[int]: list of in-play numbers
    """
    inPlayNumsStr = line.split('|')[1]
    return getNumbers( inPlayNumsStr )    

class Card:
    """ Represents one of the "Card" lines.
        Stores the cardId, score and number of copies.
    """    
    def __init__( self, cardId : int, score : int ):
        self.cardId    = cardId
        self.score     = score
        self.numCopies = 1

    def addCopies( self, copies : int ):
        """ increases the number of copies of this card by "copies" """
        self.numCopies = self.numCopies + copies
    
def letsPlayPart1( txt : str ) -> int:
    """ Part 1 - runs the number-matching game logic
         - read the input lines
         - for each line
           - get the winning numbers
           - get the in-play numbers
           - count how many in-play numbers match the winning numbers
           - score for this line is 2^(num winning cards)
           - add to total
        - return total.
    """
    lines = readLines( txt )
    accumulator = 0
    for line in lines:
        winningNums    = getWinningNumbers( line )  # left of "|"
        inPlayNums     = getInPlayNumbers( line )   # right of "|"
        
        # count the number of matches between in-play numbers and winning numbers.
        successfulNums = [num for num in inPlayNums if num in winningNums]
        
        # score is pow(2,match-count)
        score = int(math.pow( 2, len(successfulNums)-1 ))
        
        # calculate the running total.
        accumulator = accumulator + score
    return accumulator

def letsPlayPart2( txt ):
    """ Part 2 - runs the card cloning game logic """
    cards = { } # dict of cardId to score:numCards
    lines = readLines( txt )

    accumulator = 0
    for line in lines:
        # for each line, read the card number, winning numbers, in-play numbers.
        cardId         = getCardNumber( line )
        winningNums    = getWinningNumbers( line )
        inPlayNums     = getInPlayNumbers( line )

        # count the number of winning numbers and the score.        
        successfulNums = [num for num in inPlayNums if num in winningNums]
        score = len(successfulNums)
        
        # create a Card for this line to store the score.
        cards[cardId] = Card(cardId, score)

    # For each card...
    for cardId in cards:
        if cards[cardId].score > 0:
            # score is greater than zero. 
            # for the next "score" cards we get one copy for every copy of the current card.
            numClones = cards[cardId].numCopies
            for id in range( cardId+1, cardId+cards[cardId].score+1 ):
                if id in cards: # dont run past the last card.
                    cards[id].addCopies(numClones)
    
    # Finally, total up how many copies of each card we have.
    totalCards = 0
    for cardId in cards:
        totalCards = totalCards + cards[cardId].numCopies

    # return the total        
    return totalCards

