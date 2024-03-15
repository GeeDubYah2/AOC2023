from   dataset import EXAMPLE_1, PUZZLE_INPUT
from functools import reduce

def readLines( txt ):
    return [ l for l in txt.split('\n') if len(l) > 0 ]

def readValues( label, lines ):
    for line in lines:
        if label in line:
            line = line.split(':')[-1]
            while '  ' in line:
                line    = line.replace('  ', ' ' )
            numbers = line.split(' ')
            values  = [ int(num) for num in numbers if num ]
            return values

def readRaceResults( lines ):
    times     = readValues( 'Time', lines )
    distances = readValues('Distance', lines)
    return list(zip( times, distances ))

def calculateDistance( chargeTime, runTime ):
    speed    = chargeTime
    distance = speed * runTime
    return distance

def findFasterTimes( result ):
    fasterTimes = []
    time, bestDistance = result
    startChargeTime    = int(bestDistance/time)
    for chargeTime in range( startChargeTime, time):
        distance = calculateDistance( chargeTime, time-chargeTime )
        if distance > bestDistance:
            fasterTimes.append( chargeTime )
    return fasterTimes

def findFasterTimesAllRaces( results ):
    numWaysToBeatRecord = []
    for result in results:
        fasterResults = findFasterTimes( result )
        numWaysToBeatRecord.append( len(fasterResults) )
    return numWaysToBeatRecord

def run( txt ):
    lines               = readLines(txt)
    results             = readRaceResults(lines)
    numWaysToBeatRecord = findFasterTimesAllRaces( results )
    retval              = reduce((lambda x, y: x * y), numWaysToBeatRecord)
    return retval
