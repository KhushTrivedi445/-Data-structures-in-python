#Implementation of stack using oops(class)


class stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,data):
        self.top+=1
        self.stack.append(data) 
    def pop(self):
        self.top-=1
        self.stack.pop()
        return stack
    def peek(self):
         print(self.stack[self.top])
    def display(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
            print("|")
            
s=stack()

s.push(0)
s.push(1)
s.push(2)
s.push(3)

s.pop()

s.peek()

s.display()
        
