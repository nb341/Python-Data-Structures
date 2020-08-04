class Stack:
    size=0
    def __init__(self,size):
        self.size = size
        self.S = list()

    
    def push(self,x):
        self.S.append(x)

    def pop(self):
        if not self.S:
            print("Stack is empty")
        else:
           self.size-=1    
           return self.S.pop()
    
    def top(self):
        if self.S:
            print(self.S[-1])
        else:
            print("Stack is empty")
    
    def Size(self):
        self.size-=1
        return self.size
    
    def isEmpty(self):
        if self.S:
            return False
        else:
            return True

if __name__=="__main__":
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s.pop())
    #print(s.isEmpty())
    while not s.isEmpty():
        print(s.pop())
    
        

        
