class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    
class LinkedStack:
    def __init__(self):
        self.head = None 
    
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
    
    def pop(self):
        curr = self.head
        if curr == None:
            raise StackError("Stack is empty")
        self.head = curr.next
        return curr.value
    
    def peek(self):
        return self.head.value if self.head else None
    


class Error(Exception):
    pass

class StackError(Error):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)


if __name__ == '__main__':
    s = LinkedStack()
    s.push(1)
    print(s.peek())
    s.push(2)
    print(s.peek())
    s.push(3)
    print("Head is", s.peek())
    print(s.pop())
    print("Head is", s.peek())
    print(s.pop())
    print("Head is", s.peek())
    print(s.pop())
    print("Head is", s.peek())
