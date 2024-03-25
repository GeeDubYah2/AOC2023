import unittest
from day5 import (readLines, getNumbers, getSeeds, getMap, MappingEntry, getAllMappings, MAP_TYPES, performMapping,
                  performAllMappings, runPart1, getSeedRanges, SeedRange, findNextMappingEntry,
                  applyRangeMappings, mergeRanges, performRangedMappings, runPart2)
from dataset import EXAMPLE_INPUT, PUZZLE_INPUT


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
        
    def test_getSeedRanges( self ):
        # Test getSeedRanges
        lines       = readLines(EXAMPLE_INPUT)
        seedRanges  = getSeedRanges( lines )
        
        """ seeds: 79 14 55 13 """
        self.assertEqual( 2, len(seedRanges) )
        self.assertEqual( SeedRange(55, 55+13-1), seedRanges[0] ) # ranges are ordered by start value
        self.assertEqual( SeedRange(79, 79+14-1), seedRanges[1] )
        
        lines       = readLines("""seeds: 0 100 0 50 1 45""")
        seedRanges  = getSeedRanges( lines )        
        self.assertEqual( SeedRange(0, 49),  seedRanges[0] )  # ranges are ordered by start value then end
        self.assertEqual( SeedRange(0, 99), seedRanges[1] )
        self.assertEqual( SeedRange(1, 45),  seedRanges[2] )
        
        lines       = readLines("""seeds: 0 100 101 100 201 100""")
        seedRanges  = getSeedRanges( lines )        
        self.assertEqual( SeedRange(0, 99),  seedRanges[0] )  # ranges are ordered by start value then end
        self.assertEqual( SeedRange(101, 200), seedRanges[1] )
        self.assertEqual( SeedRange(201, 300),  seedRanges[2] )

    def test_runPart1(self):
        # Finally test the run method. This performs the full mapping operation on the seed values in the input text.

        # Test with the example from the AOC challenge page. Expected result is 35.
        self.assertEqual( 35, runPart1( EXAMPLE_INPUT ) ) 

        # Now run with the full PUZZLE_INPUT.
        self.assertEqual( 196167384, runPart1( PUZZLE_INPUT ) )  # <<<<<<<< PART ONE RESULT <<<<<<<<


    def test_findNextMappingEntry( self ):
        MAP = """
seed: 0 100 200 300

seed-to-soil map:
50 100 2
52 50 48
        """
        lines      = readLines(MAP)
        mapEntries = [MappingEntry.createMappingEntry(lines[4]), MappingEntry.createMappingEntry(lines[5])]
        mapEntries = sorted(mapEntries)
        
        # MappingEntry: start 50, end 97, mapOp +2
        # MappingEntry: start 100, end 101, mapOp -50

        
        print( '\n\n')
        for me in mapEntries:
            print( me )
            
        self.assertEqual( mapEntries[0], findNextMappingEntry( 45, mapEntries ) )   # before ME#1 -> ME#1
        self.assertEqual( mapEntries[0], findNextMappingEntry( 50, mapEntries ) )   # start of ME#1 -> ME#1
        self.assertEqual( mapEntries[0], findNextMappingEntry( 97, mapEntries ) )   # end of ME#1 -> ME#1
        
        self.assertEqual( mapEntries[1], findNextMappingEntry( 98,  mapEntries ) )  # before ME#2 -> ME#2
        self.assertEqual( mapEntries[1], findNextMappingEntry( 100, mapEntries ) )  # start of ME#2 -> ME#1
        self.assertEqual( mapEntries[1], findNextMappingEntry( 101, mapEntries ) )  # end of ME#2 -> ME#1
        
        self.assertEqual( None, findNextMappingEntry( 110, mapEntries ) )      # after ME#2 -> None

    def test_applyRangeMappings( self ):
        MAP = """
seeds: 0 31 50 101
    
seed-to-soil map:
10 10 11
40 40 21
90 90 21
"""
        # This will define the follow seed and mapping ranges.
        #
        # SeedRange(start=0, end=30, range=31)          - SR#1
        # SeedRange(start=50, end=150, range=101)       - SR #2
        # MappingEntry: start 10, end 20, mapOp 0       - ME #1
        # MappingEntry: start 40, end 60, mapOp 0       - ME #2
        # MappingEntry: start 90, end 110, mapOp 0      - ME #3

        # Test 1: to simplify debugging i've made all the mapOps zero.
        lines = readLines(MAP)
        seedRanges  = getSeedRanges( lines )
        mappings = getMap('seed-to-soil', lines)

        newSeedRanges = applyRangeMappings(seedRanges, mappings['seed-to-soil'])
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd( 0, 9),  newSeedRanges[0] )     # SR #1 before ME#1
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(10,20),  newSeedRanges[1] )     # overlap SR #1 and ME#1
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(21,30),  newSeedRanges[2] )     # SR#1 after ME#1
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(50,60),  newSeedRanges[3] )     # overlap of SR#2 and ME#2
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(61,89),  newSeedRanges[4] )     # SR#2 - gap between ME#2 and ME#3
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(90,110), newSeedRanges[5] )     # SR#2 overlap with ME#2
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(111,150),newSeedRanges[6] )     # SR#2 after ME#2

        MAP2 = """
seeds: 0 31 50 101
    
seed-to-soil map:
20 10 11
140 40 21
50 90 21
"""
        # This will define the follow seed and mapping ranges.
        #
        # SeedRange(start=0, end=30, range=31)          - SR#1
        # SeedRange(start=50, end=150, range=101)       - SR #2
        # MappingEntry: start 10, end 20, mapOp +10     - ME #1
        # MappingEntry: start 40, end 60, mapOp +100    - ME #2
        # MappingEntry: start 90, end 110, mapOp -40    - ME #3
        #
        # Test 2 - added mapOps. This will alter the seedRanges returned where the seedRange overlaps a mappingEntry.

        lines       = readLines(MAP2)
        seedRanges  = getSeedRanges( lines )
        mappings    = getMap('seed-to-soil', lines)

        newSeedRanges = applyRangeMappings(seedRanges, mappings['seed-to-soil'])
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(   0,   9 ), newSeedRanges[0] )  # SR #1 before ME#1
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  20,  30 ), newSeedRanges[1] )  # overlap SR #1 and ME#1 (+10)
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  21,  30 ), newSeedRanges[2] )  # SR#1 after ME#1
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd( 150, 160 ), newSeedRanges[3] )  # overlap of SR#2 and ME#2 (+100)
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  61,  89 ), newSeedRanges[4] )  # SR#2 - gap between ME#2 and ME#3
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  50,  70 ), newSeedRanges[5] )  # SR#2 overlap with ME#3 (-40)
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd( 111, 150 ), newSeedRanges[6] )  # SR#2 after ME#2

        # Test sorting of seed ranges.
        sortedRanges = sorted(newSeedRanges)
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(   0,   9 ), sortedRanges[0] )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  20,  30 ), sortedRanges[1] )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  21,  30 ), sortedRanges[2] )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  50,  70 ), sortedRanges[3] )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  61,  89 ), sortedRanges[4] )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd( 111, 150 ), sortedRanges[5] )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd( 150, 160 ), sortedRanges[6] )

        # Test the mergeRanges function too
        mergedSeedRanges = mergeRanges( newSeedRanges )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(   0,   9 ), mergedSeedRanges[0] )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  20,  30 ), mergedSeedRanges[1] )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd(  50,  89 ), mergedSeedRanges[2] )
        self.assertEqual( SeedRange.newSeedRangeFromStartEnd( 111, 160 ), mergedSeedRanges[3] )


    def test_performRangedMappings(self):
        lines       = readLines(EXAMPLE_INPUT)
        seedRanges  = getSeedRanges( lines )
        mappings    = getAllMappings( lines )

        seeds = performRangedMappings( seedRanges, mappings )
        self.assertEqual( 46, sorted(seeds)[0].start )    # From the part two example.

    def test_runPart2(self):
        self.assertEqual( 46, runPart2( EXAMPLE_INPUT )[0].start )
        self.assertEqual( 125742456, runPart2( PUZZLE_INPUT )[0].start )    # <<<<< ANSWER: Solution to part 2


if __name__ == '__main__':
    unittest.main()