import unittest
from dataset import EXAMPLE_INPUT, PUZZLE_INPUT

'''
Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
'''
HANDS = {'Five of a kind':500, 'Four of a kind':400, 'Full house':350, 'Trips':300, 'Two pairs':200, 'One pair':100, 'High card':0}
CARDS = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
UNRANKED = -1

'''
# TO BE RANKED 5 (strongest) to 1 (weakest)

# HAND BID-VALUE
32T3K  765   # PAIR           1      765 * 1  
T55J5  684   # TRIPS (T)      4      684 * 4
KK677  28    # TWO PAIR (KK)  3      28  * 3
KTJJT  220   # TWO PAIR (KT)  2      220 * 2
QQQJA  483   # TRIPS (Q)      5      483 * 5 --> 6440
'''

def readLines( txt ):
    return [ l for l in txt.split('\n') if len(l) > 0 ]

def strToInt( txt ):
    ''' converts txt to a decimal value. ignores everything thats not a digit
        'Game 51:' --> 51
    '''
    digits = [c for c in txt if c.isdigit() ]
    value  = int(''.join(digits))
    return value

def getCards( line ):
    hand = line.split(' ')[0]
    return hand

def getBid( line ):
    bid = strToInt( line.split(' ')[1] )
    return bid

class Hand:
    def __init__(self, cards, bid):
        '''
        :param cards: card string - e.g. 'AK45J'
        :param bid:   bid value - int
        '''
        self.cards = cards # e.g. 'AK45J'
        self.bid   = bid   # e.g.  123

        self.cardValues = self.setCardValues( )  # cards converted to values. 'A'->14; 'K'->13 ... '2'->2
        self.cardCounts = self.countCards( )     # count of each card (uses cardValues)
        self.score      = self.scoreHand( )      # score hand based on winning HANDS

    def __eq__(self, other):
        return (self.cards, self.bid) == (other.cards, other.bid)

    def __str__(self):
        txt = 'Cards: %s Bid: %4d Score: %3d' % (self.cards, self.bid, self.score)
        return txt

    def setCardValues( self ):
        cardValues = []
        for c in self.cards:
            cardValues.append( CARDS[c] )
        return cardValues

    class CardCount:
        def __init__(self, cardValue, count ):
            self.cardValue = cardValue
            self.count     = count

        def __lt__(self, other):
            return (self.count, self.cardValue) < (other.count, other.cardValue)

        def __eq__(self, other):
            return (self.count, self.cardValue) == (other.count, other.cardValue)

    def countCards( self ):
        '''
        cards is list of cardValues

        returns a list of tuples, (count, cardValue)
        reverse sorted - count desc, cardValue desc.
        '''
        cardCounts = []
        distinctCards = set( self.cardValues )
        for cv in distinctCards:
            cardCounts.append( self.CardCount(cv, self.cardValues.count(cv) ) )
        cardCounts = sorted(cardCounts, reverse=True)
        return cardCounts

    def scoreHand( self ):
        mostFreq   = self.cardCounts[0] # card with highest count
        secondFreq = self.cardCounts[1] if len(self.cardCounts)>1 else None # and next most frequent

        if mostFreq.count == 5:
            score = HANDS['Five of a kind']
        elif mostFreq.count == 4:
            score = HANDS['Four of a kind']
        elif mostFreq.count == 3:
            if secondFreq and secondFreq.count == 2:
                score = HANDS['Full house']
            else:
                score = HANDS['Trips']
        elif mostFreq.count == 2:
            if secondFreq and secondFreq.count == 2:
                score = HANDS['Two pairs']
            else:
                score = HANDS['One pair']
        else:
            score =  HANDS['High card']
        return score

    @classmethod
    def rankHands( cls, hands ):
        # Rank hands based on their score and then cardValues
        # Score takes precedence
        # Then first card, second card.... last card.
        rankedHands = sorted(hands, key=lambda h: (h.score, h.cardValues), reverse=True)
        return rankedHands

def parseLines( lines ):
    hands = [ ]
    for line in lines:
        cards = getCards( line )
        bid   = getBid( line )
        hands.append( Hand(cards, bid) )
    return hands

def playGame( txt ):
    lines = readLines(txt)
    hands = parseLines(lines)
    rankedHands = Hand.rankHands(hands)
    total = 0
    for idx in range(0,len(rankedHands)):
        rank  = len(rankedHands) - idx
        score = rank * rankedHands[idx].bid
        total = total + score
        print( 'Rank: %d -- %s => %6d %6d' % (rank, str(rankedHands[idx]), score, total ) )
    return total









