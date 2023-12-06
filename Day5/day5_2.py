import unittest
from dataset import EXAMPLE_INPUT, PUZZLE_INPUT

'''
seeds: 79 14 55 13          # seeds to plant

seed-to-soil map:           # destination-range-start, source-range-start, range-length
50 98 2                     # maps 98->50, 99->51                                           # 98, 99 (start+range-1), subtract 48
52 50 48                    # maps 50->52, 51->53 ... 48 entries up to 97->99               # 50, 97 (start+range-1), add 2
                            # any unlisted seeds are mapped to same soil value: 10->10

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15                            
'''

# Ordered list of map types
MAP_TYPES = ['seed-to-soil',
             'soil-to-fertilizer',
             'fertilizer-to-water',
             'water-to-light',
             'light-to-temperature',
             'temperature-to-humidity',
             'humidity-to-location',
            ]

def readLines( txt ):
    return txt.split('\n')

def getNumbers( numberSequence ):
    numStrs = numberSequence.split()
    nums = [ int(numStr) for numStr in numStrs ]
    return nums

def getSeeds( lines ):
    for line in lines:
        if line.startswith( 'seeds:'):
            numsStr = line.split(':')[-1]
            nums = getNumbers( numsStr )
            return nums

def getSeedsV2( lines ):
    seeds = []
    nums = getSeeds( lines )
    for idx in range( 0, len(nums), 2 ):
        start  = nums[idx]
        length = nums[idx+1]
        print( 'getSeedsV2: Processing %d of %d.' % (idx, len(nums)) )
        seeds = seeds + list( range(start, start+length) )
    return seeds


class MappingEntry:
    ''' Represents one row of a map - e.g.
        soil-to-fertilizer map:
        0 15 37
         ---> MappingEntry( 15, 15+37-1, -15 )
    '''
    def __init__(self, sourceStart, sourceEnd, mapOp):
        self.sourceStart = sourceStart
        self.sourceEnd   = sourceEnd
        self.mapOp       = mapOp

    @classmethod
    def createMappingEntry( cls, line ):
        mappings = getNumbers( line )
        (destStart, sourceStart, rangeLength) = tuple( mappings )
        mapping = MappingEntry( sourceStart, sourceStart+rangeLength-1, destStart-sourceStart )
        return mapping

    def applyMapping(self, sourceValue):
        if self.sourceStart <= sourceValue <= self.sourceEnd:
            return sourceValue + self.mapOp
        else:
            return -1

    def __str__(self):
        return ('MappingEntry: source start %d, end %d, dest start: %d, mapOp %s%d' %
                (self.sourceStart,
                 self.sourceEnd,
                 self.sourceStart + self.mapOp,
                 '+' if self.mapOp > 0 else '',
                 self.mapOp))

    def __eq__(self,other):
        return ((self.sourceStart, self.sourceEnd, self.mapOp)
                == (other.sourceStart, other.sourceEnd, other.mapOp))

    def __lt__(self, other):
        return self.sourceStart < other.sourceStart

def getMap(mapType, lines):
    mapEnts = []
    idx = 0
    while idx<len(lines):
        if lines[idx].startswith( mapType + ' map:'):
            idx = idx + 1
            while lines[idx].lstrip() and idx<len(lines):
                mapEnts.append( MappingEntry.createMappingEntry(lines[idx]) )
                idx = idx + 1
        else:
            idx=idx+1
    return {mapType:mapEnts}

def getAllMappings( lines ):
    allMappings = {}
    for mt in MAP_TYPES:
        allMappings[mt] = getMap(mt, lines)[mt]

    return allMappings

def performMapping( sourceVal, mapType, allMappings ):
    for mapEntry in sorted( allMappings[mapType] ):
        destVal = mapEntry.applyMapping(sourceVal)
        if destVal != -1:
            # mapping found. return the destVal.
            return destVal
        # else - continue looking for a mapping for sourceVal

    # no mappings found. just return sourceVal.
    return sourceVal

def getSrcName( mt ):
    '''
    Returns the "source" part of the mapping type name
     e.g. 'seed-to-soil' --> 'seed'
    (note: seed is actually capitalised to 'Seed')
    '''
    retval = mt.split('-')[0]
    retval = retval.replace( 'seed', 'Seed' )
    return retval

def performAllMappings( seed, allMappings ):
    value       = seed
    debugString = ''
    for mt in MAP_TYPES:
        newVal = performMapping( value, mt, allMappings )
        debugString = debugString + '%s %d, ' % ( getSrcName(mt), value )
        #print( 'Mapped %d -> %d using %s' % (value, newVal, mt ) )
        value = newVal
    debugString = debugString + 'location %d.' % value
    return value, debugString

def run( txt ):
    lines = readLines(txt)

    seeds       = getSeedsV2(lines)
    allMappings = getAllMappings(lines)
    locations   = []

    for idx in range(0,len(seeds)):
        seed = seeds[idx]
        print( 'Processing seed %d of %d. %.02f%% complete' % ( idx+1, len(seeds), (idx+1/len(seeds)*100.0) ) )
        locations.append( performAllMappings(seed, allMappings)[0] )

    return min( locations )


class TestDay5_1 (unittest.TestCase):

    def test_readLines(self):
        self.assertIn('temperature-to-humidity map:', readLines(EXAMPLE_INPUT))
        self.assertEqual(35, len(readLines(EXAMPLE_INPUT)))

    def test_getNumbers( self ):
        self.assertEqual( getNumbers('69 82 63 72 16 21 14  1 123456'), [69,82,63,72,16,21,14,1,123456] )
        self.assertEqual( getNumbers(' 69  42  '), [69,42] )
        self.assertEqual( getNumbers(''), [] )

    def test_getSeeds(self):
        lines = readLines(EXAMPLE_INPUT)
        self.assertEqual( getSeeds(lines), [79, 14, 55, 13] )

    def test_getSeedsV2(self):
        lines = [ 'seeds: 20 10 40 20' ]
        expected = list( range(20, 30) ) + list( range(40, 60) )
        self.assertEqual(getSeedsV2(lines), expected)

        lines = readLines(EXAMPLE_INPUT)
        expected = list( range(79, 79+14) ) + list( range(55, 55+13) )
        self.assertEqual( getSeedsV2(lines), expected )

    def test_getMap_1(self):
        TXT='''      
        
seed-to-soil map:
50 98 2
52 50 48 

        '''
        lines = readLines(TXT)
        maap = getMap('seed-to-soil', lines)
        self.assertIn('seed-to-soil',maap)
        self.assertEqual(2, len(maap['seed-to-soil']))
        print( [str(m) for m in maap['seed-to-soil'] ] )
        self.assertEqual(MappingEntry(98,99,-48), maap['seed-to-soil'][0])
        self.assertEqual(MappingEntry(50,97,2), maap['seed-to-soil'][1])

    def test_getMap_2(self):
        TXT = '''      
humidity-to-location map:
60 56 37
56 93 4
        '''
        lines = readLines(TXT)
        maap = getMap('humidity-to-location', lines)
        self.assertIn('humidity-to-location',maap)
        self.assertEqual(2, len(maap['humidity-to-location']))
        print( [str(m) for m in maap['humidity-to-location'] ] )
        self.assertEqual(MappingEntry(56,92,4), maap['humidity-to-location'][0])
        self.assertEqual(MappingEntry(93,96,-37), maap['humidity-to-location'][1])

    def test_getAllMappings(self):
        lines = readLines(EXAMPLE_INPUT)
        allMappings = getAllMappings( lines )
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
        lines = readLines(EXAMPLE_INPUT)
        allMappings = getAllMappings( lines )

        # performMapping( sourceVal, mapType, allMappings ):
        # FYI - copied from above...
        self.assertEqual(MappingEntry(50,97,2), allMappings['seed-to-soil'][1])
        self.assertEqual(MappingEntry(98,99,-48), allMappings['seed-to-soil'][0])

        self.assertEqual( 14,    performMapping( 14, 'seed-to-soil', allMappings ) ) # no mapping
        self.assertEqual( 79+2,  performMapping( 79, 'seed-to-soil', allMappings ) ) # apply +2 mapping
        self.assertEqual( 98-48, performMapping( 98, 'seed-to-soil', allMappings ) ) # apply -48 mapping

        # FYI...
        self.assertEqual(MappingEntry(56,92,4), allMappings['humidity-to-location'][0])
        self.assertEqual(MappingEntry(93,96,-37), allMappings['humidity-to-location'][1])

        self.assertEqual( 14,    performMapping( 14, 'humidity-to-location', allMappings ) ) # no mapping
        self.assertEqual( 92+4,  performMapping( 92, 'humidity-to-location', allMappings ) ) # apply +4 mapping
        self.assertEqual( 93-37, performMapping( 93, 'humidity-to-location', allMappings ) ) # apply -37 mapping

    def test_performAllMappings(self):
        lines       = readLines(EXAMPLE_INPUT)
        allMappings = getAllMappings( lines )

        # def performAllMappings( seed, allMappings ):
        self.assertEqual( performAllMappings(79, allMappings),
            (82, 'Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.') )
        self.assertEqual( performAllMappings(14, allMappings),
            (43, 'Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.') )
        self.assertEqual( performAllMappings(55, allMappings),
            (86, 'Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.') )
        self.assertEqual( performAllMappings(13, allMappings),
            (35, 'Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.') )

    def test_run(self):
        self.assertEqual( 46, run( EXAMPLE_INPUT ) )

    def test_run_theBigOne(self):
        # BRUTE FORCING AIN'T GOING TO WORK
        # self.assertEqual( 1, run( PUZZLE_INPUT ) )  # <<<<<<<< THE ANSWER IS HERE <<<<<<<<
        #                 ^^^^^^^^^
        pass

    def test_run_smartForcingIt( self ):
        lines       = readLines(PUZZLE_INPUT)
        allMappings = getAllMappings( lines )

        htlMaps = allMappings['humidity-to-location']
        print( '\n'.join( [str(me) for me in htlMaps] ) )

        print( [ me.sourceStart + me.mapOp for me in htlMaps ] )


if __name__ == '__main__':
    unittest.main()