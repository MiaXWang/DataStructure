class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
    
class AVLTree:
    def __init__(self):
        self.root = None
    
    def find(self, key):
        return self.find(key, self.root)


    def _find(self, key, node):
        if node is None:
            return None
        elif key < node.val:
            return self._find(key, node.left)
        elif key > node.val:
            return self._find(key, node.right)
        else:
            return node
    
    def findMin(self):
        if self.root is None:
            return
        else:
            return self._findMin(self.root)
        
    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else: return node
    
    def findMax(self):
        if self.root is None:
            return 
        else:
            return self._findMax(self.root)
    
    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else: return node

    def getHeight(self, node):
        if node is None:
            return -1
        else:
            return node.height
    
    def singleLeftRotate(self, node):
        parent = node.left
        node.left = parent.right
        parent.right = node
        node.height = max(self.getHeight(node.right), self.getHeight(node.left)) + 1
        parent.height = max(self.getHeight(parent.left), node.height) + 1
        return parent
    
    def singleRightRotate(self, node):
        parent = node.right
        node.right = parent.left
        parent.left = node
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        parent.height = max(self.getHeight(parent.right), node.height) + 1
        return parent

    def doubleLeft(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)
    
    def doubleRight(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)

        else:
            self.root = self._insert(key, self.root)

    def _insert(self, key, node):
        if node is None:
            node = Node(key)
        elif key < node.val:
            node.left = self._insert(key, node.left)
            if (self.getHeight(node.left) - self.getHeight(node.right)) == 2:
                if key < node.left.val:
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeft(node)
        elif key > node.val:
            node.right = self._insert(key, node.right)
            if (self.getHeight(node.right) - self.getHeight(node.left)) == 2:
                if key > node.right.val:
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRight(node)
        
        node.height = max(self.getHeight(node.right), self.getHeight(node.left)) + 1
        return node

    def delete(self, key):
        self.root = self._delete(key, self.root)
    
    def _delete(self, key, node):
        if node is None:
            raise KeyError("Error Key not in Tree")
        
        elif key < node.val:
            node.left = self._delete(key, node.left)
            if (self.getHeight(node.right) - self.getHeight(node.left)) == 2:
                if self.getHeight(node.right.right) > self.getHeight(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRight(node)
        
        elif key > node.val:
            node.right = self._delete(key, node.right)
            if (self.getHeight(node.left) - self.getHeight(node.right)) == 2:
                if self.getHeight(node.left) > self.getHeight(node.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeft(node)

        elif node.left and node.right:
            if node.left.height <= node.right.height:
                minNode = self._findMin(node.right)
                node.val = minNode.val
                node.right = self._delete(node.val, node.right)
            else:
                maxNode = self._findMax(node.left)
                node.val = maxNode
                node.right = self._delete(node.val, node.left)
        
        else:
            if node.right:
                node = node.right
            else:
                node = node.left
        
        return node



                

    
