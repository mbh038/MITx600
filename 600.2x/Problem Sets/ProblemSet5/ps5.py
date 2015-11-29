# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
import re # for use of regular expressions
import random
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!

# The nodes of the map are the buildings, while the weighted edges
# will be the walkways between them.
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    mitGraph = WeightedDigraph()
    
    map=open(mapFilename)
    print "Loading map from file..."
    for line in map:
        #line=line.rstrip()
        nodeCouple= [ int(i) for i in re.findall('[0-9]+',line) ]
        #print nodeCouple
        na=Node(str(nodeCouple[0]))
        nb=Node(str(nodeCouple[1]))
        edge = WeightedEdge(na, nb, nodeCouple[2],nodeCouple[3])
        try:
            mitGraph.addNode(na)
        except ValueError:
            pass
        try:
            mitGraph.addNode(nb)
        except ValueError:
            pass
        mitGraph.addEdge(edge)
        
    return mitGraph
        
#mitMap = load_map("mit_map.txt")
#print isinstance(mitMap, Digraph)
#print isinstance(mitMap, WeightedDigraph)
#print mitMap.nodes
#print mitMap.edges
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

#def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
#    """
#    Finds the shortest path from start to end using brute-force approach.
#    The total distance travelled on the path must not exceed maxTotalDist, and
#    the distance spent outdoor on this path must not exceed maxDistOutdoors.
#
#    Parameters: 
#        digraph: instance of class Digraph or its subclass
#        start, end: start & end building numbers (strings)
#        maxTotalDist : maximum total distance on a path (integer)
#        maxDistOutdoors: maximum distance spent outdoors on a path (integer)
#
#    Assumes:
#        start and end are numbers for existing buildings in graph
#
#    Returns:
#        The shortest-path from start to end, represented by 
#        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
#        where there exists an edge from n_i to n_(i+1) in digraph, 
#        for all 1 <= i < k.
#
#        If there exists no path that satisfies maxTotalDist and
#        maxDistOutdoors constraints, then raises a ValueError.
#    """
#    #TODO
def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 
    
def bruteForceSearch(graph, start, end,maxTotalDist, maxDistOutdoors):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path=[]
    shortest= None
    
    shortest=DFS (graph, start, end, path, None,maxTotalDist,maxDistOutdoors)
        
    if shortest is None:
        raise ValueError("No such path")
        return
    else:
        return shortest
    

def DFS (graph, start, end, path, shortest,maxTotalDist,maxDistOutdoors):
        path = path+[start]        
        #print 'Current DFS path:', printPath(path),totalDist(graph,path),outdoorDist(graph,path)
        if start == end:
            return path
        for node in graph.childrenOf(Node(start)):
           # print node
           # print type (node)
            if node.getName() not in path: #avoid cycles
                #print shortest
                if shortest is None or totalDist(graph,path) < totalDist(graph,shortest):# 
                    newPath = DFS(graph, node.getName(),end,path,shortest,maxTotalDist,maxDistOutdoors)
                    if newPath != None and outdoorDist(graph,newPath)<=maxDistOutdoors and totalDist(graph,newPath) <=maxTotalDist:
                        if shortest is None: 
                            shortest = newPath
                        elif totalDist(graph,newPath) < totalDist(graph,shortest):
                            shortest = newPath
                        else:
                            pass                      
        return shortest
        
def totalDist(graph,path):
    """Assumes path is a list of nodes"""
    totalDist=0    
    for i in range(len(path)-1):
        for d in graph.edges[Node(path[i])]:
            if d[0]==Node(path[i+1]):
                totalDist +=float(d[1][0])
    return totalDist    
 
def outdoorDist(graph,path):
    """Assumes path is a list of nodes"""
    outdoorDist=0    
    for i in range(len(path)-1):
        for d in graph.edges[Node(path[i])]:
            if d[0]==Node(path[i+1]):
                outdoorDist +=float(d[1][1])
    return outdoorDist 
    
#path=['32','56'] 
#print len(path)
#print totalDist(mitMap,path)
#print outdoorDist(mitMap,path)
#print mitMap.edges[Node('32')]      

def search(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return bruteForceSearch(graph, start, end)

def testSP():
    mitMap = load_map("mit_map.txt")
    #nodes=mitMap.nodes
    #na=random.choice(nodes)
    #nb=random.choice(nodes)
    sp = search(mitMap, '32', '56')
    print 'Shortest path found by DFS:', printPath(sp)

#testSP()
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    path=[]
    shortest= None
    
    shortest=DFS (digraph, start, end, path, None,maxTotalDist,maxDistOutdoors)
        
    if shortest is None:
        raise ValueError("No such path")
        return
    else:
        return shortest

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
##     Test cases
#
    mitMap = load_map("mit_map.txt")
#   print isinstance(mitMap, Digraph)
#   print isinstance(mitMap, WeightedDigraph)
#   print 'nodes', mitMap.nodes
#    print 'edges', mitMap.edges


    LARGE_DIST = 1000000

#    Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    #dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
#    print "DFS: ", dfsPath1
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#    Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST,0)
    #dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    #print "DFS: ", dfsPath2
    #print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#    Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
#    print "DFS: ", dfsPath3
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#    Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#   dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
#   print "DFS: ", dfsPath4
#   print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#    Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
#    print "DFS: ", dfsPath5
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#    Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
#    print "DFS: ", dfsPath6
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
#    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
#    try:
#        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#    except ValueError:
#        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
#    print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
        
#    try:
#        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#    except ValueError:
#        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
#    print "Did DFS search raise an error?", dfsRaisedErr


# Grader Test 6
map2=WeightedDigraph()
n1=Node("1")
n2=Node("2")
n3=Node("3")
n4=Node("4")
map2.addNode(n1)
map2.addNode(n2)
map2.addNode(n3)
map2.addNode(n4)
e1=WeightedEdge(n1,n2,10.0,5.0)
e2=WeightedEdge(n1,n4,5.0,1.0)
e3=WeightedEdge(n2,n3,8.0,5.0)
e4=WeightedEdge(n4,n3,8.0,5.0)
map2.addEdge(e1)
map2.addEdge(e2)
map2.addEdge(e3)
map2.addEdge(e4)

map3=WeightedDigraph()
n1=Node("1")
n2=Node("2")
n3=Node("3")
n4=Node("4")
map3.addNode(n1)
map3.addNode(n2)
map3.addNode(n3)
map3.addNode(n4)
e1=WeightedEdge(n1,n2,10,5)
e2=WeightedEdge(n1,n4,15,1)
e3=WeightedEdge(n2,n3,8,5)
e4=WeightedEdge(n4,n3,8,5)
map3.addEdge(e1)
map3.addEdge(e2)
map3.addEdge(e3)
map3.addEdge(e4)


#print bruteForceSearch(map2, "1", "3", 100, 100)
#print bruteForceSearch(map2, "1", "3", 18, 18)
#print bruteForceSearch(map2, "1", "3", 15, 15)
#print bruteForceSearch(map2, "1", "3", 10, 10)
bruteForceSearch(map3, "1", "3", 18, 18)
#['1', '2', '3']
#bruteForceSearch(map3, "1", "3", 18, 0)
#bruteForceSearch(map3, "1", "3", 10, 10)
