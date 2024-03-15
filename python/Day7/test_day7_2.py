import unittest

from dataset import EXAMPLE_INPUT, PUZZLE_INPUT
from day7_2  import *


class TestDay5_2 (unittest.TestCase):

    def test_readLines(self):
        self.assertIn('QQQJA 483', readLines(EXAMPLE_INPUT))
        self.assertEqual(5, len(readLines(EXAMPLE_INPUT)))

    def test_strToInt(self):
        self.assertEqual( 1, strToInt('Game 1'))
        self.assertEqual( 1, strToInt('Game 1:'))
        self.assertEqual( 1, strToInt('1'))
        self.assertEqual( 1, strToInt('asdfasdf1asdasdasdf'))
        self.assertEqual( 1234, strToInt('G1234F_ '))
        self.assertEqual( 123, strToInt('1a2b3c '))

    def test_getCards( self ):
        line = '32T3K 765'
        self.assertEqual( getCards( '32T3K 765' ), '32T3K' )

    def test_getCardValues( self ):
        hand = Hand('32T3K', 0)
        self.assertEqual( hand.cardValues, [3,2,10,3,13] )

    def test_getBid( self ):
        line = '32T3K 765'
        self.assertEqual( getBid( '32T3K 765' ), 765 )

    def test_Hand( self ):
        hand = Hand( 'AKQ23', 123 )
        self.assertEqual( hand.cards, 'AKQ23' )
        self.assertEqual( hand.bid,   123 )
        self.assertEqual( hand.cardValues, [14,13,12,2,3] )
        #self.assertEqual( hand.cardCounts, [(1, 14), (1, 13), (1, 12), (1, 3), (1, 2)] )
        expectedCardCounts = [
            Hand.CardCount(14, 1),
            Hand.CardCount(13, 1),
            Hand.CardCount(12, 1),
            Hand.CardCount(3,  1),
            Hand.CardCount(2,  1),
            ]
        self.assertEqual( hand.cardCounts, expectedCardCounts )

    def test_parseLines( self ):
        lines = readLines( EXAMPLE_INPUT )
        hands = parseLines( lines ) # list of Hand objects
        self.assertEqual( 5, len(hands) )

        expectedCards = ['32T3K','T55J5','KK677','KTJJT','QQQJA']
        self.assertEqual( expectedCards, [ hand.cards for hand in hands ] )

        expectedBids  = [765,684,28,220,483]
        self.assertEqual( expectedBids, [ hand.bid for hand in hands ] )

        # First hand: '32T3K' -> [3,2,10,3,13]
        expectedCardValues = [3,2,10,3,13]
        self.assertEqual( expectedCardValues, hands[0].cardValues )

        # First hand: '32T3K' -> [(2, 3), (1, 13), (1, 10), (1, 2)] # Two threes; One 13(K), 10(T) & 2
        expectedCardCounts = [
            Hand.CardCount(3,  2),
            Hand.CardCount(13, 1),
            Hand.CardCount(10, 1),
            Hand.CardCount(2,  1),
            ]
        self.assertEqual( expectedCardCounts, hands[0].cardCounts )

    def test_Hand_countCardsAndScore( self ):
        # Ace Trips
        hand1 = Hand( 'AKJAA', 0 )
        self.assertEqual( hand1.cardCounts, [Hand.CardCount(14,3), Hand.CardCount(13,1), Hand.CardCount( 1, 1 ) ] )
        self.assertEqual( hand1.score,      HANDS['Four of a kind'] )

        hand2 = Hand( '2K2A2', 0 )
        self.assertEqual( hand2.cardCounts, [Hand.CardCount(2,3), Hand.CardCount(14,1), Hand.CardCount( 13, 1 ) ] )
        self.assertEqual( hand2.score,      HANDS['Trips'] )


        hand3 = Hand( 'AAAAA', 0 )
        self.assertEqual( hand3.cardCounts, [Hand.CardCount(14, 5)] )
        self.assertEqual( hand3.score,      HANDS['Five of a kind'] )

        hand4 = Hand( '234KA', 0 )
        self.assertEqual( hand4.cardCounts, [ Hand.CardCount(14, 1),
                                            Hand.CardCount(13, 1),
                                            Hand.CardCount(4, 1),
                                            Hand.CardCount(3, 1),
                                            Hand.CardCount(2, 1),
                                            ] )
        self.assertEqual( hand4.score,      HANDS['High card'] )

        hand5 = Hand( '234KQ', 0 ) # identical to hand4 except for last card.
        self.assertEqual( hand4.cardCounts, [ Hand.CardCount(14, 1),
                                            Hand.CardCount(13, 1),
                                            Hand.CardCount(4, 1),
                                            Hand.CardCount(3, 1),
                                            Hand.CardCount(2, 1),
                                            ] )
        self.assertEqual( hand4.score,      HANDS['High card'] )

        hand6 = Hand( 'JJJJJ', 0 ) # identical to hand4 except for last card.
        self.assertEqual( hand6.cardCounts, [ Hand.CardCount(1, 5) ] )
        self.assertEqual( hand6.score,      HANDS['Five of a kind'] )

        hand7 = Hand( '2JJJJ', 0 ) # identical to hand4 except for last card.
        self.assertEqual( hand7.cardCounts, [ Hand.CardCount(1, 4),
                                              Hand.CardCount(2, 1) ] )
        self.assertEqual( hand7.score,        HANDS['Five of a kind'] )

        # Test ranking based on score and highest-first-card.
        # Rank above is...
        # hand3 (AAAAA), hand7 (2JJJJ), hand6 (JJJJJ) - (5ofAKind)
        # hand1 - (four)
        # hand2 - (trips)
        # hand4 (234KA), hand5 (234KQ) - highcard
        hands = [hand7,hand6,hand5,hand4,hand3,hand2,hand1]
        self.assertEqual( Hand.rankHands(hands), [hand3, hand7, hand6, hand1, hand2, hand4, hand5] )

    def test_playGame( self ):
        self.assertEqual( 5905, playGame( EXAMPLE_INPUT ) )

        self.assertEqual(254083736, playGame(PUZZLE_INPUT))     #### THE ANSWER IS HERE

if __name__ == '__main__':
    unittest.main()