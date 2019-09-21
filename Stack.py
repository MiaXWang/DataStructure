#Implementation of Stack

class ArrayStack:
    def __init__(self, initialCapacity):
        self.defaultCap = 15
        if initialCapacity <= 0:
            self.capacity = defaultCap
        else:
            self.capacity = initialCapacity
        self.__top = -1
        self.__array = [None] * self.capacity
    
    def isEmpty(self):
        return self.__top == -1
    
    def push(self, e):
        if self.__top == self.capacity-1:
            raise StackError("Stack has overflowed")
        self.__top += 1
        self.__array[self.__top] = e
    
    def pop(self):
        res = self.peek()
        self.__array[self.__top] = None
        self.__top -= 1
        return res


    def peek(self):
        if self.isEmpty():
            raise StackError("Stack is Empty")
        return self.__array[self.__top]
    
    def getStack(self):
        print(self.__array)
        #return self.__array
    

# Define StackError
class Error(Exception):
    pass

class StackError(Error):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)
    

if __name__ == '__main__':
    s = ArrayStack(3)
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.pop()
    s.getStack()
