import unittest
from   day5_1  import readLines, getNumbers, getSeeds, getMap, MappingEntry, getAllMappings, MAP_TYPES, performMapping, performAllMappings, run
from   dataset import EXAMPLE_INPUT, PUZZLE_INPUT

class TestDay5_1 (unittest.TestCase):

    def test_readLines(self):
        # test the readlines function.
        self.assertIn('temperature-to-humidity map:', readLines(EXAMPLE_INPUT))
        self.assertEqual(35, len(readLines(EXAMPLE_INPUT)))

    def test_getNumbers( self ):
        # test the getNumbers function.
        # converts a string containing numbers to an integer list.
        self.assertEqual( getNumbers('69 82 63 72 16 21 14  1 123456'), [69,82,63,72,16,21,14,1,123456] )
        self.assertEqual( getNumbers(' 69  42  '), [69,42] )
        self.assertEqual( getNumbers(''), [] )

    def test_getSeeds(self):
        # Test the get seeds function.
        # Returns the integers from the line beginning "seeds:". 
        lines = readLines(EXAMPLE_INPUT)
        self.assertEqual( getSeeds(lines), [79, 14, 55, 13] )

    def test_getMap_1(self):
        # test the getMap method with a simple example.
        # blank lines should be ignored.
        # should return two MappingEntry objects.
        TXT='''      
        
seed-to-soil map:
50 98 2
52 50 48 

        '''
        lines = readLines(TXT)
        mtMap = getMap('seed-to-soil', lines)
        self.assertIn('seed-to-soil',mtMap)
        self.assertEqual(2, len(mtMap['seed-to-soil']))
        print( [str(m) for m in mtMap['seed-to-soil'] ] )
        self.assertEqual(MappingEntry(98,99,-48), mtMap['seed-to-soil'][0])
        self.assertEqual(MappingEntry(50,97,2), mtMap['seed-to-soil'][1])

    def test_getMap_2(self):
        # test the getMap method with a second example.
        # should return two MappingEntry objects.
        TXT = '''      
humidity-to-location map:
60 56 37
56 93 4
        '''
        lines = readLines(TXT)
        mtMap = getMap('humidity-to-location', lines)
        self.assertIn('humidity-to-location',mtMap)
        self.assertEqual(2, len(mtMap['humidity-to-location']))
        print( [str(m) for m in mtMap['humidity-to-location'] ] )
        self.assertEqual(MappingEntry(56,92,4), mtMap['humidity-to-location'][0])
        self.assertEqual(MappingEntry(93,96,-37), mtMap['humidity-to-location'][1])

    def test_getAllMappings(self):
        # Test the getAllMappings method using the EXAMPLE_INPUT from the AOC2023 page.
        # "allMappings" should contain entries for each map type.
        lines = readLines(EXAMPLE_INPUT)
        allMappings = getAllMappings( lines )
        self.assertEqual( len(allMappings), len(MAP_TYPES) ) # do we have an entry for every MAP_TYPE ?
        self.assertIn('seed-to-soil', allMappings )
        self.assertIn('water-to-light', allMappings)
        self.assertIn('humidity-to-location', allMappings)

        print( allMappings['light-to-temperature'] )
        self.assertEqual( 3, len( allMappings['light-to-temperature'] ) )

        self.assertEqual(MappingEntry(98,99,-48), allMappings['seed-to-soil'][0])
        self.assertEqual(MappingEntry(50,97,2), allMappings['seed-to-soil'][1])

        self.assertEqual(MappingEntry(56,92,4), allMappings['humidity-to-location'][0])
        self.assertEqual(MappingEntry(93,96,-37), allMappings['humidity-to-location'][1])

    def test_performMappings(self):
        # Test the performMappings function using the EXAMPLE_INPUT from the AOC2023 page and some seed values.
        # "allMappings" should contain entries for each map type.
        lines = readLines(EXAMPLE_INPUT)
        allMappings = getAllMappings( lines )

        # for information - the mappings we'll be testing below...
        self.assertEqual(MappingEntry(50,97,2), allMappings['seed-to-soil'][1])
        self.assertEqual(MappingEntry(98,99,-48), allMappings['seed-to-soil'][0])

        # Test some seed-to-soil mappings...
        self.assertEqual( 14,    performMapping( 14, 'seed-to-soil', allMappings ) ) # no mapping
        self.assertEqual( 79+2,  performMapping( 79, 'seed-to-soil', allMappings ) ) # apply +2 mapping
        self.assertEqual( 98-48, performMapping( 98, 'seed-to-soil', allMappings ) ) # apply -48 mapping

        # for information - the mappings we'll be testing below...
        self.assertEqual(MappingEntry(56,92,4), allMappings['humidity-to-location'][0])
        self.assertEqual(MappingEntry(93,96,-37), allMappings['humidity-to-location'][1])

        # Test some humidity-to-location mappings...
        self.assertEqual( 14,    performMapping( 14, 'humidity-to-location', allMappings ) ) # no mapping
        self.assertEqual( 92+4,  performMapping( 92, 'humidity-to-location', allMappings ) ) # apply +4 mapping
        self.assertEqual( 93-37, performMapping( 93, 'humidity-to-location', allMappings ) ) # apply -37 mapping

    def test_performAllMappings(self):
        # Test the performAllMappings function using the EXAMPLE_INPUT from the AOC2023 page and its seed values.
        lines       = readLines(EXAMPLE_INPUT)
        allMappings = getAllMappings( lines )
        seeds       = getSeeds( lines )

        # test using the examples on the AOC page.
        self.assertEqual( performAllMappings(79, allMappings),
            (82, 'Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.') )
        self.assertEqual( performAllMappings(14, allMappings),
            (43, 'Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.') )
        self.assertEqual( performAllMappings(55, allMappings),
            (86, 'Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.') )
        self.assertEqual( performAllMappings(13, allMappings),
            (35, 'Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.') )

    def test_run(self):
        # Finally test the run method. This performs the full mapping operation on the seed values in the input text.

        # Test with the example from the AOC challenge page. Expected result is 35.
        self.assertEqual( 35, run( EXAMPLE_INPUT ) ) 

        # Now run with the full PUZZLE_INPUT.
        self.assertEqual( 196167384, run( PUZZLE_INPUT ) )  # <<<<<<<< PART ONE RESULT <<<<<<<<

if __name__ == '__main__':
    unittest.main()