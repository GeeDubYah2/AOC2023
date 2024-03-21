import logging
import unittest
from   dataset import EXAMPLE_INPUT, PUZZLE_INPUT


'''
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
 - distance to ZZZ is two -> return
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

def followDirections( nodes : dict [ str : tuple[str:str] ], directions : str ) -> int:
    """ Starting at "AAA" follow the RL directions until we reach "ZZZ". Count the steps.
        :return int : step count
    """
    locn  = 'AAA'
    steps = 0
    while locn!='ZZZ':
        nextNodes = nodes[locn]
        locn      = nextNodes[0] if directions[ steps % len(directions) ] == 'L' else nextNodes[1]
        steps     = steps + 1
    return steps

def runPart1( txt : str ) -> int:
    lines      = readLines(txt)
    directions = getDirections( lines[0] )
    nodes      = readNodes( lines[1:] )
    steps      = followDirections( nodes, directions  )
    return steps
