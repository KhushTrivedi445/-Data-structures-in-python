def push(x):
    global length
    if length<limit:
        arr.append(x)
        length+=1
        print("Data pushed")
    else:
        print("Stack overflow")

def pop():
    global length
    if length>0:
       arr.pop()
       length-=1
       print("Data poped")
    else :
        print("Stack underflow")
    
def peek():
        if length==0:
         print("Stack boundary error")
        else:
            print(arr[length-1])
        
def display():
    if length==0:
        print("Stack boundary error")
    else :
        print(arr)
        
        



arr=[]
length=0
limit=5

while True :
    print("1:push")
    print("2:pop")
    print("3:peek")
    print("4:display")
    ch=int(input("Enter you choice : "))
    
    if ch==1:
        x=int(input("Enter the data you want to push"))
        push(x)
    elif ch==2:
        pop()
    elif ch==3:
        peek()
    elif ch==4:
        display()
    else :
        print("Invalid choice")
        
        
