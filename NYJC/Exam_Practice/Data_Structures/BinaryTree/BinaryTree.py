class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def remove(self):
        def relink_children(current, child):
            if current.parent:
                if child:
                    child.parent = current.parent
                if current.parent.left == current:
                    current.parent.left = child
                elif current.parent.right == current:
                    current.parent.right = child

        if self.left and self.right:
                successor = self.right.find_min()
                self.key = successor.key
                successor.remove()
        elif self.left:
            relink_children(self, self.left)
        elif self.right:
            relink_children(self, self.right)
        else:
            relink_children(self, None)

    def preorder(self):
        res = []

        res.append(self.key)
        if self.left:
            res.append(self.left.preorder())
        if self.right:
            res.append(self.right.preorder())

        return res

    def inorder(self):
        res = []

        if self.left:
            res.append(self.left.inorder())
        res.append(self.key)
        if self.right:
            res.append(self.right.inorder())

        return res

    def postorder(self):
        res = []

        if self.left:
            res.append(self.left.postorder())
        if self.right:
            res.append(self.right.postorder())
        res.append(self.key)

        return res



class BinaryTree(self):
    def __init__(self):
        self.root = None

    def getNode(self, key):
        if self.root:
            current = self.root

            while current.key != key:
                if key < current.key and current.left:
                    current = current.left
                elif key > current.key and current.right:
                    current = current.right
                else:
                    return None
            
            return current

    def removeNode(self, key):
        node = self.getNode(key)
        if self.root == node and self.root.left is None and self.root.right is None:
            self.root = None
        else:
            node.remove()

    def insert(self, key):
        new = Node(key)
        if self.root:
            self.root = new
        else:
            current = self.root

            while current.key != key:
                if key < current.key:
                    if current.left:
                        current = current.left
                    else:
                        current.left = new
                        new.parent = current.left
                elif key > current.key:
                    if current.right:
                        current = current.right
                    else:
                        current.right = new
                        new.parent = current.right
