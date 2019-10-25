class AVLNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    def set(self, currentSide, child):
        if currentSide != 'left' and currentSide != 'right':
            return False
        if currentSide == 'left':
            self.left = child
        else:
            self.right = child
        if child is not None:
            child.parent = self
        self.updateHeight()
        return True

    def balance(self):
        heightOfLeft = -1
        if self.left is not None:
            heightOfLeft = self.left.height
        heightOfRight = -1
        if self.right is not None:
            heightOfRight = self.right.height
        return heightOfLeft - heightOfRight

    def updateHeight(self):
        heightOfLeft = -1
        if self.left is not None:
            heightOfLeft = self.left.height
        heightOfRight = -1
        if self.right is not None:
            heightOfRight = self.right.height
        self.height = max(heightOfLeft, heightOfRight) + 1

    def replace(self, current, new):
        if self.left is current:
            return self.set('left', new)
        elif self.right is current:
            return self.set('right', new)
        return False


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
        else:
            current = self.root
            while current is not None:
                if node.key < current.key:
                    if current.left is None:
                        current.left = node
                        node.parent = current
                        current = None
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        node.parent = current
                        current = None
                    else:
                        current = current.right
            node = node.parent
            while node is not None:
                self.calibrate(node)
                node = node.parent

    def rotateToTheleft(self, node):
        rightOfLeft = node.right.left

        if node.parent is not None:
            node.parent.replace(node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        node.right.set('left', node)
        node.set('right', rightOfLeft)
        return node.parent

    def rotateToTheRight(self, node):
        leftOfRight= node.left.right
        if node.parent is not None:
            node.parent.replace(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        node.left.set('right', node)
        node.set('left', leftOfRight)
        return node.parent

    def calibrate(self, node):
        node.updateHeight()
        if node.balance() == -2:
            if node.right.balance() == 1:
                self.rotateToTheRight(node.right)
            return self.rotateToTheleft(node)
        elif node.balance() == 2:
            if node.left.balance() == -1:
                self.rotateToTheleft(node.left)
            return self.rotateToTheRight(node)
        return node



    def search(self, key):
        current = self.root
        while current is not None:
            if current.key.lower() == key.lower():
                return current
            elif current.key < key:
                current = current.right
            else:
                current = current.left
        return None

