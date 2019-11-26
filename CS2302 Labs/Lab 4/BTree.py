# code is Olac Fuentes' from last semester when I had him with few changes
class BTreeNode:
    # Constructor
    def __init__(self, keys=[], children=[], isLeaf=True, maxKeys=5):
        self.keys = keys
        self.children = children
        self.isLeaf = isLeaf
        if maxKeys < 3:  # maxKeys must be odd and greater or equal to 3
            maxKeys = 3
        if maxKeys % 2 == 0:  # maxKeys must be odd and greater or equal to 3
            maxKeys += 1
        self.maxKeys = maxKeys

    def is_full(self):
        return len(self.keys) >= self.maxKeys


class BTree:
    def __init__(self, maxKeys=5):
        self.maxKeys = maxKeys
        self.root = BTreeNode(maxKeys=maxKeys)

    def find_child(self, k, node=None):
        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if k < node.keys[i]:
                return i
        return len(node.keys)

    def insert_internal(self, i, node=None):

        if node is None:
            node = self.root

        # node cannot be Full
        if node.isLeaf:
            self.insert_leaf(i, node)
        else:
            k = self.find_child(i, node)
            if node.children[k].is_full():
                m, l, r = self.split(node.children[k])
                node.keys.insert(k, m)
                node.children[k] = l
                node.children.insert(k + 1, r)
                k = self.find_child(i, node)
            self.insert_internal(i, node.children[k])

    def split(self, node=None):
        if node is None:
            node = self.root
        mid = node.maxKeys // 2
        if node.isLeaf:
            left_child = BTreeNode(node.keys[:mid], maxKeys=node.maxKeys)
            right_child = BTreeNode(node.keys[mid + 1:], maxKeys=node.maxKeys)
        else:
            left_child = BTreeNode(node.keys[:mid], node.children[:mid + 1], node.isLeaf,
                                   maxKeys=node.maxKeys)
            right_child = BTreeNode(node.keys[mid + 1:], node.children[mid + 1:], node.isLeaf,
                                    maxKeys=node.maxKeys)
        return node.keys[mid], left_child, right_child

    def insert_leaf(self, i, node=None):
        if node is None:
            node = self.root

        node.keys.append(i)
        node.keys.sort()

    def leaves(self, node=None):
        if node is None:
            node = self.root
        if node.isLeaf:
            return [node.keys]
        s = []
        for c in node.children:
            s = s + self.leaves(c)
        return s

    def insert(self, i, node=None):
        if node is None:
            node = self.root
        if not node.is_full():
            self.insert_internal(i, node)
        else:
            m, l, r = self.split(node)
            node.keys = [m]
            node.children = [l, r]
            node.isLeaf = False
            k = self.find_child(i, node)
            self.insert_internal(i, node.children[k])

    def height(self, node=None):
        if node is None:
            node = self.root
        if node.isLeaf:
            return 0
        return 1 + self.height(node.children[0])

    def contains(self, k):
        result = self.search(k)
        if result is None:
            return False
        return True

    def search(self, k, node=None):
        if node is None:
            node = self.root
        if k in node.keys:
            return node
        if node.isLeaf:
            return None
        return self.search(k, node.children[self.find_child(k, node)])

    def print_d(self, space, node=None):
        if node is None:
            node = self.root
        if node.isLeaf:
            for i in range(len(node.keys) - 1, -1, -1):
                print(space, node.keys[i])
        else:
            self.print_d(space + '   ', node.children[len(node.keys)])
            for i in range(len(node.keys) - 1, -1, -1):
                print(space, node.keys[i])
                self.print_d(space + '   ', node.children[i])