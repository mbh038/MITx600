# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)
        
class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


class WeightedEdge(Edge):
    def __init__(self,src,dest,weight1,weight2):
        Edge.__init__(self,src,dest)
        self.weight1=weight1
        self.weight2=weight2
    def getTotalDistance(self):
        return self.weight1
    def getOutdoorDistance(self):
        return self.weight2
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest,self.weight1,self.weight2)


class WeightedDigraph(Digraph):
    """
    A directed graph including weights on edges
    """
    def __init__(self):
        Digraph.__init__(self)
    def addEdge(self, WeightedEdge):
        src = WeightedEdge.getSource()
        dest = WeightedEdge.getDestination()
        weight1 = WeightedEdge.getTotalDistance()
        weight2 = WeightedEdge.getOutdoorDistance()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        nodeList=[]
        nodeList.append(dest)
        nodeList.append((weight1,weight2))
        self.edges[src].append(nodeList)
    def childrenOf(self, node):
        childrenList=[]
        for d in self.edges[node]:
            childrenList.append(d[0])
        return childrenList
    def __str__(self):
        res = ''
        for k in self.edges.keys():
            for d in self.edges[k]:
            #print self.edges[k]
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, k, d[0],float(d[1][0]),float(d[1][1]))
        return res[:-1]

### Test Code
#g = WeightedDigraph()
#na = Node('a')
#nb = Node('b')
#nc = Node('c')
#g.addNode(na)
#g.addNode(nb)
#g.addNode(nc)
#e1 = WeightedEdge(na, nb, 15, 10)
#print e1
## a->b (15, 10)
#print e1.getTotalDistance()
## 15
#print e1.getOutdoorDistance()
## 10
#e2 = WeightedEdge(na, nc, 14, 6)
#e3 = WeightedEdge(nb, nc, 3, 1)
#print e2
## a->c (14, 6)
#print e3
## b->c (3, 1)
#g.addEdge(e1)
#g.addEdge(e2)
#g.addEdge(e3)
#print g
##a->b (15.0, 10.0)
## a->c (14.0, 6.0)
## b->c (3.0, 1.0)
#
## Test One
#print
#na = Node('a')
#nb = Node('b')
#nc = Node('c')
#e1 = WeightedEdge(na, nb, 15, 10)
#print isinstance(e1, Edge)# True
#print isinstance(e1, WeightedEdge)# True
#print e1.getSource()#: a
#print e1.getDestination()#: b
#print e1.getTotalDistance()#: 15
#print e1.getOutdoorDistance()#: 10
#
## Test Three
#print
#na = Node('a')
#nb = Node('b')
#nc = Node('c')
#g = WeightedDigraph()
#print isinstance(g, Digraph)#: True
#print isinstance(g, WeightedDigraph)#: True
#g.addNode(na)
#g.addNode(nb)
#print g.hasNode(na)#: True
#print g.hasNode(nb)#: True
#print g.hasNode(nc)#: False
#
## Test Five
#print
#nh = Node('h')
#nj = Node('j')
#nk = Node('k')
#nm = Node('m')
#ng = Node('g')
#g = WeightedDigraph()
#g.addNode(nh)
#g.addNode(nj)
#g.addNode(nk)
#g.addNode(nm)
#g.addNode(ng)
#randomEdge = WeightedEdge(nk, nm, 27, 20)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nk, nh, 81, 23)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, nh, 33, 20)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, nm, 24, 18)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nk, nh, 70, 69)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, nh, 94, 56)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nk, nm, 78, 66)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, nk, 71, 23)
#g.addEdge(randomEdge)
#print g.childrenOf(nh)#: []
#print g.childrenOf(nj)#: [h, m, h, k]
#print g.childrenOf(nk)#: [m, h, h, m]
#print g.childrenOf(nm)#: []
#print g.childrenOf(ng)#: []
#
#
## Test 7
#nj = Node('j')
#nk = Node('k')
#nm = Node('m')
#ng = Node('g')
#randomEdge = WeightedEdge(nm, ng, 30, 12)
#print randomEdge
##m->g (30, 12)
#randomEdge = WeightedEdge(nk, ng, 81, 22)
#print randomEdge
##k->g (81, 22)
#randomEdge = WeightedEdge(nk, ng, 76, 75)
#print randomEdge
##k->g (76, 75)
#randomEdge = WeightedEdge(nk, ng, 46, 28)
#print randomEdge
##k->g (46, 28)
#randomEdge = WeightedEdge(nm, ng, 77, 53)
#print randomEdge
##m->g (77, 53)
#
#
## Test 8
#nx = Node('x')
#ny = Node('y')
#nz = Node('z')
#e1 = WeightedEdge(nx, ny, 18, 8)
#e2 = WeightedEdge(ny, nz, 20, 1)
#e3 = WeightedEdge(nz, nx, 7, 6)
#g = WeightedDigraph()
#g.addNode(nx)
#g.addNode(ny)
#g.addNode(nz)
#g.addEdge(e1)
#g.addEdge(e2)
#g.addEdge(e3)
#print g
##y->z (20.0, 1.0)
##x->y (18.0, 8.0)
##z->x (7.0, 6.0)