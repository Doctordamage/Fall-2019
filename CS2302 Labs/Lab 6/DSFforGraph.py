class DisjointSetForest:
    def __init__(self, n):
        self.forest = [-1] * n

    def isValid(self, index):
        return 0 <= index < len(self.forest)

    def find(self, a):
        if not self.isValid(a):
            return -1
        if self.forest[a] < 0:
            return a
        return self.find(self.forest[a])

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.forest[rb] = ra



