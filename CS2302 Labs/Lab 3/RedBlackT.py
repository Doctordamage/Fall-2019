class RBTNode:
    def __init__(self, key, parent, Red=False, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        if Red:
            self.color = 'red'
        else:
            self.color = 'black'

    def ColorB(self):
        return self.color == 'black'

    def ColorR(self):
        return self.color == 'red'

    def set(self, currentSide, child):
        if currentSide != 'left' and currentSide != 'right':
            return False
        if currentSide == 'left':
            self.left = child
        else:
            self.right = child

    def FindGrandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    def FindSibling(self):
        if self.parent is not None:
            if self is self.parent.left:
                return self.parent.right
            return self.parent.left
        return None

    def FindUncle(self):
        grandparent = self.FindGrandparent()
        if grandparent is None:
            return None
        if grandparent.left is self.parent:
            return grandparent.right
        return grandparent.left
    def count(self):
        count = 1
        if self.left is not None:
            count = count + self.left.count()
        if self.right is not None:
            count = count + self.right.count()
        return count

class RBT:
    def __init__(self):
        self.root = None

    def __len__(self):
        if self.root is None:
            return 0
        return self.root.count()

    def insert(self, key):
        new = RBTNode(key, None, True, None, None)
        self.insertHelper(new)

    def insertHelper(self, node):
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while current is not None:
                if node.key < current.key:
                    if current.left is None:
                        current.set('left', node)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.set('right', node)
                        break
                    else:
                        current = current.right
        node.color = 'red'
        self.balance(node)
    def balance(self, node):
        if node.parent is None:
            node.color = 'black'
            return
        if node.parent.ColorB():
            return
        parent = node.parent
        grandparent = node.FindGrandparent()
        uncle = node.FindUncle()
        if uncle is not None and uncle.ColorR():
            parent.color = uncle.color = 'black'
            grandparent.color = 'red'
            self.balance(grandparent)
            return
        if node is parent.right and parent is grandparent.left:
            self.rotateToTheleft(parent)
            node = parent
            parent = node.parent
        elif node is parent.left and parent is grandparent.right:
            self.rotateToTheRight(parent)
            node = parent
            parent = node.parent
        parent.color = 'black'
        grandparent.color = 'red'
        if node is parent.left:
            self.rotateToTheRight(grandparent)
        else:
            self.rotateToTheleft(grandparent)

    def rotateToTheleft(self, node):
        rightOfLeft = node.right.left
        if node.parent is not None:
            node.parent.replace(node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        node.right.set('left', node)
        node.set('right', rightOfLeft)

    def rotateToTheRight(self, node):
        leftOfRight = node.left.right
        if node.parent is not None:
            node.parent.replace(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        node.left.set('right', node)
        node.set('left', leftOfRight)

    def search(self, key):
        current = self.root
        while current is not None:
            if current.key == key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None
