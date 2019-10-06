class TrieTree:
    def __init__(self):
        self.root = {}
        self.end = -1

    def insert(self, word):
        currNode = self.root
        for w in word:
            if w not in currNode:
                currNode[w] = {}
            currNode = currNode[w]
        currNode[self.end] = True
    
    def search(self, word):
        currNode = self.root
        for w in word:
            if w not in currNode:
                return False
            currNode = currNode[w]
        
        if self.end not in currNode:
            return False
        
        return True

    def startWith(self, prefix):
        currNode = self.root
        for w in prefix:
            if w not in currNode:
                return False
            currNode = currNode[w]
        return True

