"""
Advent Of Code - Day 6 Parts 1 & 2.

Boat races: https://adventofcode.com/2023/day/6

Time:      7  15   30
Distance:  9  40  200

 - read the time and distance-records for each race. The input above represents three races.
 - the toy boat needs to be charged before it can complete a race.
   - one millisecond of charging -> results in 1mm/ms speed
   - try different charging periods to find the number of ways to beat the record distance for that race.

 - e.g. race #1 - time=7ms best-distance=9mm
    - charging for 2ms -> 2mm/ms -> distance of 10mm. This is better than the 9mm best-distance.

 - find the number of chargingTimes (int values) that give a distance > best-distance.
"""

from   dataset import EXAMPLE_1, PUZZLE_INPUT_1
from functools import reduce

def readLines( txt : str ) -> list[str]:
    """
    Read lines from input
    :param txt: input
    :return:    list[ str ]
    """
    return [ l for l in txt.split('\n') if len(l) > 0 ]

def readValues( label : str, lines : list[str] ) -> list[int]:
    """
    Reads integer values from a line after a colon symbol.

    e.g. readValues( 'a_label', lines )
    a_label: 1 2 3 4
      --> [1,2,3,4]

    :param label:  label at the start of the line
    :param lines:  all lines
    :return:       list[int]
    """
    for line in lines:
        if label in line:
            line = line.split(':')[-1]
            while '  ' in line:
                line    = line.replace('  ', ' ' )
            numbers = line.split(' ')
            values  = [ int(num) for num in numbers if num ]
            return values

def readRaceResults( lines : list[str] ) -> list[ tuple[int, int] ]:
    """
    Reads the values from the time and distance results' lines.

    :param lines: list[str]
    :return:      list[ tuple(int, int ) ] -- list of time/distance pairs. one per race.
    """
    times     = readValues( 'Time', lines )
    distances = readValues('Distance', lines)
    return list(zip( times, distances ))

def calculateDistance( chargeTime : int, runTime : int ) -> int :
    """
    Calculates distance for a given chargeTime/runTime.

    :param chargeTime: change time (ms) -> equivalent to speed
    :param runTime:    runtime (ms)

    :return: distance, where distance = speed * runTime.
    """
    speed    = chargeTime
    distance = speed * runTime
    return distance

def findFasterTimes( result : tuple[int, int] ) -> list[int] :
    """
    Try different chargeTimes from (bestDistance / time) to time.
    Calculate distance for each chargeTime
    if its better than bestDistance then add it to the fasterTimes list.

    :param result: tuple containing time/bestDistance for this race.
    :return: list of chargeTimes that give a greater distance than bestDistance.
    """
    fasterTimes = []
    time, bestDistance = result
    startChargeTime    = int(bestDistance/time)
    for chargeTime in range( startChargeTime, time):
        distance = calculateDistance( chargeTime, time-chargeTime )
        if distance > bestDistance:
            fasterTimes.append( chargeTime )
    return fasterTimes

def findFasterTimesAllRaces( results : list[ tuple[int, int] ] ) -> list[int]:
    """
    For each race:
        - Try different chargeTimes from (bestDistance / time) to time.
        - Calculate distance for each chargeTime
        - if its better than bestDistance then add it to the fasterTimes list.

    :param result: tuple containing time/bestDistance for this race.
    :return: list of chargeTimes that give a greater distance than bestDistance.
    """
    numWaysToBeatRecord = []
    for result in results:
        fasterResults = findFasterTimes( result )
        numWaysToBeatRecord.append( len(fasterResults) )
    return numWaysToBeatRecord

def run( txt : str ) -> int :
    """
    Part 1 & 2...

    Process all the race results in txt.
    Find chargeTimes that beat the distance in the race result.

    :param txt: puzzle input
    :return:    "number of ways you can beat the record"
    """
    lines               = readLines(txt)
    results             = readRaceResults(lines)
    numWaysToBeatRecord = findFasterTimesAllRaces( results )
    retval              = reduce((lambda x, y: x * y), numWaysToBeatRecord)
    return retval
