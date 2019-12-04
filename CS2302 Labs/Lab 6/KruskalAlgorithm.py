from GraphAdjacencyMatrix import *
from DSFforGraph import *

class Edge(object):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def kruskal(g: GraphAM):
    listOfEdges = list()
    for i in range(len(g.am)):
        for j in range(len(g.am[i])):
            if g is None:
                return 'error'
            elif g.am[i][j] != 0:
                listOfEdges.append(Edge(i, j, g.am[i][j]))
    listOfEdges = sorted(listOfEdges, key=lambda currentEdge: currentEdge.weight)
    set1 = DisjointSetForest(len(g.am))
    finalEdges = set()
    for i in range(len(listOfEdges)):
        if set1 is None:
            return 'error'
        elif set1.find(listOfEdges[i].dest) != set1.find(listOfEdges[i].src):
            finalEdges.add(listOfEdges[i])
            set1.union(listOfEdges[i].src, listOfEdges[i].dest)
    finalGraph = GraphAM(len(g.am), g.weighted, g.directed)
    if finalEdges is None:
        return'error'
    else:
        for current in finalEdges:
            finalGraph.insert_edge(current.dest, current.src, current.weight)
    return finalGraph


