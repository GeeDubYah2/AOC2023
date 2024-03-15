import unittest

from   dataset import EXAMPLE_INPUT, PUZZLE_INPUT
from   enum import Enum
import logging

'''
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''

def readLines( txt ):
    return [ l for l in txt.split('\n') if len(l) > 0 ]

def getDirections( line ):
    assert( line.count('L') + line.count('R') == len(line) )
    return line

def readNode( line ):
    nodeKey   = line.split('=')[0].replace(' ','')
    nodeLeft  = line.split('=')[1].split(',')[0].replace('(','').replace(' ','')
    nodeRight = line.split('=')[1].split(',')[1].replace(')', '').replace(' ', '')
    return nodeKey, (nodeLeft, nodeRight)

def readNodes( lines ):
    nodes = {}
    for line in lines:
        if '=' in line:
            nodes.setdefault( *readNode(line) )
    return nodes

def followDirections( nodes, directions ):
    locn  = 'AAA'
    steps = 0
    while locn!='ZZZ':
        nextNodes = nodes[locn]
        locn      = nextNodes[0] if directions[ steps % len(directions) ] == 'L' else nextNodes[1]
        steps     = steps + 1
    return steps

def followGhostDirections( startLocn, endLocns, nodes, directions, maxSteps=10000 ):
    locn  = startLocn
    steps = 0

    while steps < maxSteps:
        nextNodes = nodes[locn]
        locn      = nextNodes[0] if directions[ steps % len(directions) ] == 'L' else nextNodes[1]

        steps     = steps + 1
        if locn[-1]=='Z':
            endLocns.add( steps )

        if locn==startLocn:
            break
    return locn

def runPart1( txt ):
    lines      = readLines(txt)
    directions = getDirections( lines[0] )
    nodes      = readNodes( lines[1:] )
    steps      = followDirections( nodes, directions  )
    return steps

def runPart2( txt ):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

    lines      = readLines(txt)
    directions = getDirections( lines[0] )
    nodes      = readNodes( lines[1:] )

    startingNodes = [ n for n in nodes if n[-1]=='A' ]
    endLocnsDict  = {} # dict of startLocn to endLocns
    for locn in startingNodes:
        endLocns = set()
        endLocnsDict[locn] = endLocns

        logging.info( 'Calling followGhostDirection: %s', locn )
        followGhostDirections( locn, endLocns, nodes, directions, 100000000 )
        logging.info('endLocns for %s: length: %d', locn, len(endLocns) )

    locn =  startingNodes.pop()
    combinedEndLocns = endLocnsDict[ locn ]

    while startingNodes:
        locn = startingNodes.pop()
        logging.info('Calculating intersection for: %s', locn)
        combinedEndLocns.intersection_update( endLocnsDict[ locn ] )
    return sorted( combinedEndLocns )[0]

    #
    # for locn in endLocnsDict:
    #     for s in endLocnsDict[locn]:
