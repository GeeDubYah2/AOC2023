import logging
import unittest
from   dataset import PART1A_EXAMPLE, PUZZLE_INPUT
from   math import lcm


'''
AOC problem page: https://adventofcode.com/2023/day/8

Puzzle input consists of right/left directions and then a map consisting of nodes (e.g. AAA) and the left/right destinations from that node.
We need to follow the right/left direction from AAA until we reach ZZZ.
The right/left directions repeat.

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)

Part 1:
 - start at AAA
 - use the RL indication to pick the next step. in this case "R" to get to CCC
 - then from CCC pick L to get to ZZZ
 - continue looping through the RL directions until you reach ZZZ (in this example no looping is needed)
 - distance to ZZZ is two -> return this value.
 
 Part 2 - see runPart2( ) below.
'''

def readLines( txt : str ) -> list[str]:
    """ split txt into lines. ignore blank lines. return as list[str]
    """
    return [ l for l in txt.split('\n') if len(l) > 0 ]

def getDirections( line : str ) -> str:
    """ returns the RL instructions on line
    """
    assert( line.count('L') + line.count('R') == len(line) )
    return line

def readNode( line : str ) -> tuple[str : tuple[str : str ] ]:
    """ Reads a node from the current line.
        Node looks something like this...
        
            AAA = (BBB, CCC)
        
        nodeKey   = AAA
        nodeLeft  = BBB
        nodeRight = CCC
        
    returns (nodeKey, (nodeLeft, nodeRight)) as a tuple[str : tuple[str : str ] 
    """
    nodeKey   = line.split('=')[0].replace(' ','')
    nodeLeft  = line.split('=')[1].split(',')[0].replace('(','').replace(' ','')
    nodeRight = line.split('=')[1].split(',')[1].replace(')', '').replace(' ', '')
    return nodeKey, (nodeLeft, nodeRight)

def readNodes( lines : list[str] ) -> dict [ str : tuple[str:str] ]:
    """ Reads in all nodes from lines
    
        These are returned as a dictionary nodeKey : (nodeLeft, nodeRight)
        :return  dict [ str : tuple[str:str] ]
    """
    nodes = {}
    for line in lines:
        if '=' in line:
            nodes.setdefault( *readNode(line) )
    return nodes

def followDirections( allNodes : dict [ str : tuple[str:str] ], directions : str ) -> int:
    """ Starting at "AAA" follow the RL directions until we reach "ZZZ". Count the steps.
        :return int : step count
    """
    locn  = 'AAA'
    steps = 0
    while locn!='ZZZ':
        nextNodes = allNodes[locn]
        locn      = nextNodes[0] if directions[ steps % len(directions) ] == 'L' else nextNodes[1]
        steps     = steps + 1
    return steps

def runPart1( txt : str ) -> int:
    """ Runs part1 of the day8 problem
    
        :return int : number of steps to reach ZZZ.
    """    
    lines      = readLines(txt)
    directions = getDirections( lines[0] )
    allNodes   = readNodes( lines[1:] )
    steps      = followDirections( allNodes, directions  )
    return steps

def runPart2( txt : str, maxSteps : int = 100 ) -> int:
    """ Runs part2 of the day8 problem
    
    - as in part 1...
      - read lines
      - read the directions
      - read the node definitions
    - find all starting nodes. these end with "A" - e.g. xxA
    - follow directions for each of these start points until we hit an endpoint. these end in Z - e.g. xxZ
    - if these directions are followed repeatedly (they must loop). How many steps until every start point reaches an end-point simultaneously?
    - if we can calculate how many steps it takes each start-point to repeat - i.e. its period.
    - the simultaneous end point will be the lowest common multiple of all periods.   

    :param str txt: puzzle input
    :return int: number of steps to the simultaneous end-point.
    """
    lines           = readLines(txt)
    directions      = getDirections( lines[0] )
    allNodes        = readNodes( lines[1:] )
    
    # Find all the starting nodes. These end in an "A".
    startingNodes   = [ n for n in allNodes if n[-1]=='A' ]
    ghostTrailSteps = {}
    
    # for each starting node...
    for startNode in startingNodes:
        steps = 0
        node  = startNode
        ghostTrailSteps[startNode] = []
        
        # complete maxSteps iterations
        while steps < maxSteps:
            
            # move to the next position
            direction  = 0 if directions[ steps % len(directions) ] == 'L' else 1
            node   = allNodes[node][direction]
            
            # check if its an end point and record the number of steps to get here.
            if node[-1]=='Z':
                ghostTrailSteps[startNode].append(steps+1)
            
            steps = steps+1
        msg = '%s, %s' % (startNode, ghostTrailSteps[startNode])
        print( 'Number of steps: ' + msg )
    
    # Calculate the number of steps between each of the end points.
    # This gap appears to be the same so we must be in a repeating pattern.
    # The gap is therefore the repeating period.
    periodicity = []
    print( '\n\nPeriodicity:' )
    for startNode in startingNodes:
        msg = startNode
        for i in range(1, len(ghostTrailSteps[startNode])):
            msg = msg + ', ' + str(ghostTrailSteps[startNode][i] - ghostTrailSteps[startNode][i-1])
        print( msg )
        
        periodicity.append( ghostTrailSteps[startNode][1] - ghostTrailSteps[startNode][0] )
    
    print( '\nperiodicity for each start point: ' + str(periodicity) )
    
    # all starting points will reach an endpoint at the lowest common multiple of all periods.
    # fortunately the math library has a handy function to calculate this.
    retval = lcm( *periodicity )
    print( retval )
    return retval
