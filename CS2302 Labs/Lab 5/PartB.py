import math
class MaximumHeap(object):
    def __init__(self):
        self.tree = []

    def size(self):
        return len(self.tree)
    def fileReader(file):
        dictionary = {}
        heap = MaximumHeap()
        with open(file, encoding='windows-1252') as fileName:
            for line in fileName:
                word = str(line.split())[2:len(str(line.split())) - 2]
                if word in dictionary:
                    count = dictionary.get(word) + 1
                    temp = {word: count}
                    dictionary.update(temp)
                else:
                    dictionary[word] = 1
        for key in dictionary:
            heap.insert([key, dictionary[key]])
        return heap, dictionary

    def insert(self, item):
        self.tree.append(item)
        self.percolateUp(len(self.tree) - 1)

    def findParent(self, index):
        if index == 0:
            return -math.inf
        parent = self.tree[(index - 1) // 2]
        return parent[1]

    def rightChild(self, index):
        child = 2 * index + 2
        if child >= len(self.tree):
            return -math.inf
        currentChild = self.tree[child]
        return currentChild[1]

    def leftChild(self, index):
        child = 2 * index + 1
        if child >= len(self.tree):
            return -math.inf
        currentChild = self.tree[child]
        return currentChild[1]

    def findRoot(self):
        if len(self.tree) == 1:
            return self.tree.pop()
        root = self.tree[0]
        self.tree[0] = self.tree.pop()
        self.percolateDown(0)
        return root

    def percolateUp(self, index):
        if index == 0:
            return
        indexOfParent = (index - 1) // 2
        valueOfParent = self.tree[indexOfParent]
        IndexOfValue = self.tree[index]
        if valueOfParent[1] < IndexOfValue[1]:
            IndexOfValue[0], valueOfParent[0] = valueOfParent[0], IndexOfValue[0]
            IndexOfValue[1], valueOfParent[1] = valueOfParent[1], IndexOfValue[1]
            self.percolateUp(indexOfParent)

    def percolateDown(self, index):
        IndexOfValue = self.tree[index]
        if IndexOfValue[1] >= max(self.leftChild(index), self.rightChild(index)):
            return
        if self.leftChild(index) > self.rightChild(index):
            indexOfChild = 2 * index + 1
        else:
            indexOfChild = 2 * index + 2
        maximum = self.tree[indexOfChild]
        IndexOfValue[0], maximum[0] = maximum[0], IndexOfValue[0]
        IndexOfValue[1], maximum[1] = maximum[1], IndexOfValue[1]
        self.percolateDown(indexOfChild)



    def caseCompare(self, temp):
        listOfLowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
        listOfUpperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
        for index in range(len(listOfUpperCase)):
            if (temp == listOfUpperCase[index]):
                temp2 = listOfLowerCase[index]
                return temp2
        return temp

    def printInDescendingOrder(self, size):
        for index in range(size):
            word = self.findRoot()
            print('Word:')
            print(word[0])
            print('times repeated:')
            print(word[1])
            print()
