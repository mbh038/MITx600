# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:01:09 2015

@author: Mike
"""

# Finding the Shortest Path Using Brute Force

def search(digraph, start, end, maxTotalDist, maxDistOutdoors):
    q = [(0, 0, [start])]
    while q:
        td, od, path = q.pop()
        if path[-1] == end:
            yield td, to, path         # Yield all paths
            continue
        for n, (nd, no) in digraph.childrenOf(Node(path[-1])):
            td += nd
            od += no
            if n.name in path:
                continue               # Avoid loops
            if td > maxTotalDist or od > maxDistOutdoors:
                continue               # Skip paths over max distances
            q.append((nd, no, path+[n.name]))

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    td, od, path = min(search(digraph, start, end, maxTotalDist, maxDistOutdoors))
    return path

  
#    These are all pretty standard graph search algorithms, because this implementation is
#   always poping off the backit is effectively a Stack data structure which is a standard
#    Depth First Search [DFS] search. If you were to pop(0)from the front then it would be a
#    Queue data structure which implements a Breadth First Search [BFS] (Note: list.pop(0)is
#    inefficient and it would be better to use collection.deque instead of a list for q and
#    deque.popLeft())