class GraphAM:

    def __init__(self, vertices, weighted=False, directed=False):
        self.am = []
        for i in range(vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.am.append([0] * vertices)
        self.directed = directed
        self.weighted = weighted
        self.representation = 'AM'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.am)

    def insert_vertex(self):
        for lst in self.am:
            lst.append(0)

        new_row = [0] * (len(self.am) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
        self.am.append(new_row)

        return len(self.am) - 1  # Return new vertex id

    def insert_edge(self, src, dest, weight=1):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.am[src][dest] = weight

        if not self.directed:
            self.am[dest][src] = weight

    def num_vertices(self):
        return len(self.am)

    def FindInDegree(self):
        inDegree = [0] * len(self.am)
        for i in range(len(self.am)):
            for j in range(len(self.am[i])):
                if self.am[i][j] != 0:
                    inDegree[j] += 1
        return inDegree

    def AdjacentVertices(self, temp):
        vertices = list()
        for i in range(len(self.am[temp])):
            if self.am[temp][i] != 0:
                vertices.append(i)
        return vertices