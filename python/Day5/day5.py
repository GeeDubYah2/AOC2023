from copy import copy
from dataclasses import dataclass

'''
AOC2023 Day5 challenge:     https://adventofcode.com/2023/day/5

To summarise:
    - read the seeds value from the puzzle input
    - apply the mappings as defined in the input text
    - find the lowest resulting value
    - return this value.
    
---

PUZZLE_INPUT:
=============

seeds: 79 14 55 13          # seeds to plant

seed-to-soil map:           # destination-range-start, source-range-start, range-length
50 98 2                     # maps 98->50, 99->51      2 entries only                       # 98, 99 (start+range-1), subtract 48
52 50 48                    # maps 50->52, 51->53 ... 48 entries up to 97->99               # 50, 97 (start+range-1), add 2
                            # any unlisted seeds are mapped to same soil value: 10->10

soil-to-fertilizer map:
0 15 37                     # map 15->0, 16->1, 17->2 ... 37 entries in this range.         # 15, 51 (15+37-1), subtract 15.
37 52 2                     # map 52->37
39 0 15                     # map 0->39
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
    """
    Read the test input and convert to list of lines (strings)
    """
    return txt.split('\n')


def getNumbers( numberSequence ):
    """
    Convert a string containing a space delimited list of numbers to a [int].
     e.g. getNumbers(' 69  42  ') --> [69,42]
    Ignores any extra spaces.

    :param numberSequence:  ' 69  42  '
    :return: [int]
    """
    numStrs = numberSequence.split()
    nums = [ int(numStr) for numStr in numStrs ]
    return nums


def getSeeds( lines ):
    """
    Parses the seeds line (the first line)...
     e.g. "seeds: 79 14 55 13"

    Returns list of seed numbers.
    :param lines:
    :return: seed numbers as an [int]
    """

    for line in lines:
        if line.startswith( 'seeds:'):
            numsStr = line.split(':')[-1]
            nums = getNumbers( numsStr )
            return nums


class MappingEntry:
    """ Represents one row of a map - e.g.
        from the soil-to-fertilizer map:
        0 15 37
         ---> MappingEntry( 15, 15+37-1, -15 )
           ---> sourceStart      = 15
           ---> sourceEnd        = 51
           ---> mappingOperation = subtract 15 (maps 15->0, 16->1... 51->36)
    """
    def __init__(self, sourceStart, sourceEnd, mapOp):
        self.sourceStart = sourceStart
        self.sourceEnd   = sourceEnd
        self.mapOp       = mapOp

    @classmethod
    def createMappingEntry( cls, line ):
        """ Class method. Creates a MappingEntry from a line containing a mapping.
            e.g. 0 15 37 --> MappingEntry( 15, 15+37-1, 0-15 ) --> MappingEntry( 15, 51, -15 )
        """
        mappings = getNumbers( line )
        (destStart, sourceStart, rangeLength) = tuple( mappings )
        mapping = MappingEntry( sourceStart, sourceStart+rangeLength-1, destStart-sourceStart )
        return mapping

    def applyMapping(self, sourceValue):
        """ Applies the mapOp (add or subtract N) to sourceValue if sourceValue is within range of this mapping.
            Returns sourceValue + mapOp -> int
        """
        if self.sourceStart <= sourceValue <= self.sourceEnd:
            return sourceValue + self.mapOp
        else:
            return -1

    def __str__(self):
        """ Return the MappingEntry as a string. See formatting below. """
        return ('MappingEntry: start %d, end %d, mapOp %s%d' %
                (self.sourceStart,
                 self.sourceEnd,
                 '+' if self.mapOp > 0 else '',
                 self.mapOp))

    def __eq__(self,other):
        """ Equality function """
        return ((self.sourceStart, self.sourceEnd, self.mapOp)
                == (other.sourceStart, other.sourceEnd, other.mapOp))

    def __lt__(self, other):
        """ Less than function. Order by sourceStart """
        return self.sourceStart < other.sourceStart

###################################################################################################################################################


def getMap(mapType, lines):
    """
    Finds the specified map and parses its entries.

    e.g. For mapType="seed-to-soil map" find the corresponding section in the lines input.

    seed-to-soil map:
    50 98 2
    52 50 48

    Then return a MappingEntry for each set of mappings defined (in this case two).

    :return: dict { mapType : list[ MappingEntry ] }
    """
    mapEntries = []
    idx = 0
    while idx<len(lines):
        if lines[idx].startswith( mapType + ' map:'):
            idx = idx + 1
            while lines[idx].lstrip() and idx<len(lines):
                mapEntries.append( MappingEntry.createMappingEntry(lines[idx]) )
                idx = idx + 1
        else:
            idx=idx+1
    return {mapType:mapEntries}

def getAllMappings( lines ):
    """
    Read the input lines. Find all map definitions and return as a dictionary keyed by mapType.
    :param lines:
    :return: dict { mapType : list[ MappingEntry ] }
    """
    allMappings = {}
    for mt in MAP_TYPES:
        allMappings[mt] = getMap(mt, lines)[mt]

    return allMappings

def performMapping( sourceVal, mapType, allMappings ):
    """
    Perform the mappings specified for mapType on the int values in sourceVal.

    e.g. for mapType = "seed-to-soil"...

    seed-to-soil map:
    50 98 2             --> MappingEntry( 98, 99, -48 )  ME#1
    52 50 48            --> MappingEntry( 50, 97, +2  )  ME#2

    so for sourceVals [1, 53, 98, 100]
          1 -->   1    outside of range for both MEs
         53 -->  55    due to ME #2
         98 -->  50    due to ME #1
        100 --> 100    outside of range for both MEs

          --> return [1,55,50,100]

    :param sourceVal:       the input values
    :param mapType:         which mappings are to be applied
    :param allMappings:     dict containing all mappings.
    :return:                mapped values as [int]
    """
    for mapEntry in sorted( allMappings[mapType] ):
        destVal = mapEntry.applyMapping(sourceVal)
        if destVal != -1:
            # mapping found. return the destVal.
            return destVal
        # else - continue looking for a mapping for sourceVal

    # no mappings found. just return sourceVal.
    return sourceVal

def getSrcName( mt ):
    """
    Returns the "source" part of the mapping type name
     e.g. 'seed-to-soil' --> 'seed'
    (note: seed is actually capitalised to 'Seed')
    """
    retval = mt.split('-')[0]
    retval = retval.replace( 'seed', 'Seed' )
    return retval

def performAllMappings( seed, allMappings ):
    """
    Perform all mappings in the order specified in MAP_TYPES on the input value "seed".
    
    :param seed:            value to be mapped
    :param allMappings:     dict containing all mappings. Keyed by mapType.
    :return:                the mapped value (int).
    """
    value       = seed
    debugString = ''
    for mt in MAP_TYPES:
        newVal = performMapping( value, mt, allMappings )
        debugString = debugString + '%s %d, ' % ( getSrcName(mt), value )
        #print( 'Mapped %d -> %d using %s' % (value, newVal, mt ) )
        value = newVal
    debugString = debugString + 'location %d.' % value
    return value, debugString

def runPart1( txt ):
    """ Main entry point. 
        Parse the lines in input txt. Extract the seed values. Map them. Return the lowest value.    
    :param txt: input text
    :return:    lowest location number
    """
    lines = readLines(txt)

    seeds       = getSeeds(lines)
    allMappings = getAllMappings(lines)

    locations = [ performAllMappings(seed, allMappings)[0] for seed in seeds ]
    return min( locations )


@dataclass( order=True )
class SeedRange:
    """
    Part 2: Represents a range of seed/location values.
    """
    start : int
    end   : int

    @classmethod
    def newSeedRange(cls, start : int, valueRange : int) -> 'SeedRange':
        """ Creates a new SeedRange based on start and range-of-values """
        return SeedRange(start, start + valueRange - 1)

    @classmethod
    def newSeedRangeFromStartEnd( cls, start : int, end : int ) -> 'SeedRange':
        """ Creates a new SeedRange based on start and end values """
        return SeedRange( start, end )

def getSeedRanges(lines):
    """
    Parses the seeds line (the first line)...
     e.g. "seeds: 79 14 55 13"

    Returns list of seed numbers.
    :param lines:
    :return: seed numbers as an [int]
    """
    seedRanges = []
    for line in lines:
        if line.startswith( 'seeds:'):
            numsStr = line.split(':')[-1]
            nums = getNumbers( numsStr )
            while nums:
                start = nums.pop(0)
                range = nums.pop(0)
                seedRanges.append( SeedRange.newSeedRange(start, range) )
            return sorted( seedRanges )


def findNextMappingEntry( value, mapping ):
    """
    Scans "mapping" (list of MappingEntries) looking for the MappingEntry that includes value or comes immediately after
    value.
    :param value:   value to search for
    :param mapping: list of MappingEntries

    :return:        a MappingEntry
    """
    retval = None
    for me in mapping:
        if value > me.sourceEnd:
            # skip this mapping entry
            continue
        elif value <= me.sourceEnd:
            # value is before or within current mapping entry
            return me
    
    # No mappingEntries overlapping or after value.
    return None


def applyRangeMappings(seeds, mapping):
    """ Split the seed ranges to match the mappings.
        Then create new seed ranges with MappingEntry.mapOp applied.

    :param _type_ seeds:    list of SeedRanges
    :param _type_ mapping:  list of MapEntries
    :return:                new list of SeedRanges
    """
    newSeedRanges = []
    
    # split the seed ranges to match the mappings.
    for seedRange in seeds:

        start = seedRange.start
        end   = seedRange.end

        while start < end:
            me = findNextMappingEntry( start, mapping )

            if me:
                if start < me.sourceStart:
                    # before the start of me. create a new seed range
                    newSeedRanges.append( SeedRange.newSeedRangeFromStartEnd( start, min(end, me.sourceStart-1) ) )

                    # update "start" to the beginning of me.
                    start = me.sourceStart

                # inside me range
                elif start >= me.sourceStart:
                    # create a new seed range. adjust start and end based on mapping entry mapOp.
                    newSeedRanges.append( SeedRange.newSeedRangeFromStartEnd( start+me.mapOp, min(end, me.sourceEnd)+me.mapOp ) )

                    # update "start" to the end of me.
                    start = min(end, me.sourceEnd) + 1

            else:
                # me is None, so we must be after last mapping.
                newSeedRanges.append( SeedRange.newSeedRangeFromStartEnd(start, end) )

                # update "start" to be "end. This will terminate the while loop
                start = end

    return newSeedRanges


def mergeRanges( seedRanges ):
    """
    Processes the ranges in "seedRanges". Any contiguous or overlapping ranges are merged.

    :return: merged, sorted list of seedRanges.
    """
    newSeedRanges = []
    for sr in sorted(seedRanges):
        if not newSeedRanges:
            # first range. just add it to NSR.
            newSeedRanges.append(sr)
            continue

        if sr.start <= newSeedRanges[-1].end:
            # overlap between sr and the last seedRange. extend the last seedRange in NSR.
            newSeedRanges[-1].end = max( sr.end, newSeedRanges[-1].end )
        else:
            # Gap between this SR and the last SR. Append SR to NSR.
            newSeedRanges.append( sr )

    return newSeedRanges


def performRangedMappings( seeds, allMappings ):
    """ For each mapping type. Apply the mappings to seed ranges.

    :param list[SeedRanges] seeds: list of SeedRanges
    :param dict[str, list[MappingEntry] ] allMappings: table of all mappings
    """
    for mt in MAP_TYPES:
        mapping = sorted( allMappings[mt] )
        seeds   = applyRangeMappings( seeds, mapping )
        seeds   = mergeRanges( seeds )
    return seeds


def runPart2( txt ):
    """
    The seeds line now contains ranges rather than individual values, so...

    seeds: 79 14 55 13

     - range 1 - start: 79 range: 14 --> 79..92
     - range 2 - start: 55 range: 13 --> 55..67

    Keep the seeds as a list of ranges.
    Perform mappings by splitting ranges based on next level mappings. Convert start and end values based on mapOp. Merge overlapping & contiguous ranges. Repeat with next map.

    ```
    seeds:       0 100 101 100 201 100
    seed-to-soil:
                 50  100 201
                 251 151 249

    seed-to-foo map:    0..50(0); 50..250(+50); 251..500(-150)

    seeds:              0..99;            101..199;  201..299
    split ranges:       0..50;  51..99;   101..199;  201..250;  251..299   # split seed ranges to match mappings
    mapOps              +0....  +50...........................  -150....
    apply mapOp:        0..50; 101..149;  151..249;  251..300;  101..149   # apply the mapOp based on the corresponding mapping

    sort:               0..50; 101..149;  101..149;  151..249;  251..300   # sort based on start values.
    merge:              0..50; 101..149;  151..249;  251..300              # merge contiguous and overlapping ranges.
    ```

    repeat with remaining mappings

    once we have location ranges. sort and find start of first range.

    functions:
    - read seed ranges
    - split and apply mapOp on ranges.
    - sort and merge ranges
    """
    lines       = readLines( txt )
    seedRanges  = getSeedRanges( lines )
    mappings    = getAllMappings( lines )

    seeds = performRangedMappings( seedRanges, mappings )

    # return the final seed values.
    return seeds

    