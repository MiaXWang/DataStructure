class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val, curr = self.root ):    
        if not self.root:
            self.root = Node(val)
        else:
            if curr.val > val:
                if curr.left is None:
                    curr.left = Node(val)
                else:
                    self.insert(val, curr.left)
            
            elif curr.val < val: # we are not handling == situation
                if curr.right is None:
                    curr.right = Node(val)
                else:
                    self.insert(val, curr.right)

    def find(self, val):
        parent = self.root
        while parent:
            if parent.val == val:
                return True, None, parent
            elif parent.left and val == parent.left.val:
                return True, parent, parent.left
            elif parent.right and val == parent.right.val:
                return True,  parent, parent.right
            parent = parent.left if parent.val > val else parent.right
        return False, None, None

    def delete(self, val):
        _, parent, curr = self.find(val)
        if not _:
            return False
        if not curr.left and  not curr.right:
            if parent.left == curr:
                parent.left = None
            elif parent.right == curr:
                parent.right ==None
            return True
        if curr.left and curr.right:
            right = curr.right
            while right.left:
                right = right.left
            temp = right.val
            delete(self, val)
            cur.val = temp
            return True
                
        if curr.left or curr.right:
            if parent.left == curr: 
                parent.left = curr.left if curr.left else curr.right
            elif parent.right == curr:
                parent.right = curr.right if curr.right else curr.left
            return True
    
    def PreOrdertraverse(self, node):
        if node:
            print (node.val)
            self.PreOrdertraverse(self, node.left)
            self.PreOrdertraverse(self, node.right)
    
    def InOrdertraverse(self, node):
        if node:
            self.InOrdertraverse(self, node.left)
            print(node.val)
            self.InOrdertraverse(self, node.right)

    def PostOrdertraverse(self, node):
        if node:     
            self.PostOrdertraverse(self, node.left)
            self.PostOrdertraverse(self, node.right)
            print(node.val)


        



        
            