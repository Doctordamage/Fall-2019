from GraphAdjacencyMatrix import *

def topologicalSort(graph):
    inDegree = graph.FindInDegree()
    sortedList = []
    currentQueue = []
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            currentQueue.insert(0, i)
    while len(currentQueue) != 0:
        u = currentQueue.pop()
        sortedList.append(u)
        if sortedList is None:
            return 'error'
        else:
            for next in graph.AdjacentVertices(u):
                inDegree[next] -= 1
                if inDegree[next] == 0:
                    currentQueue.insert(0, next)
    if len(sortedList) != graph.num_vertices():
        return None
    return sortedList