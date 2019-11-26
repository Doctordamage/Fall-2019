class Node(object):
    def __init__(self, key, value, previous=None, next=None, empty=False):
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next
        self.empty = empty

class LRU(object):
    def __init__(self, maxCap, size=0, head=None, tail=None, table={}):
        self.size = size
        self.head = head
        self.tail = tail
        self.table = table
        self.maxCap = maxCap
        self.count = 0

    def size(self):
        return self.count

    def maxCap(self):
        return self.maxCap

    def put(self, key, value):
        node = Node(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.count += 1
        elif self.count < self.maxCap:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.count += 1
        else:
            del self.table[self.head.key]
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.head = self.head.next
            self.head.previous = None
        self.table[key] = node

    def get(self, key):
        current = self.table.get(key)
        if current == None:
            return -1
        return current.value

    def print(self):
        if self.head is None:
            print('This is empty')
            return
        temp = self.head
        while (temp != None):
            print('Key:')
            print(temp.key)
            print('Key Value:')
            print(temp.value)
            print()
            temp = temp.next
