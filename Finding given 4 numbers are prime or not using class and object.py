
class prime:
    def __init__(self,num):
        self.num=num
        if self.num==1:
            print("1 is neither composite nor prime")
            return 
        
        print(self.num,"is",end=" ",sep="@")
        count=0
        for i in range (1,self.num+1):
            if self.num%i==0:
                count+=1
        
        if count==2:
                print("prime number")
        else :
                print("not a prime number")
       
n1=prime(3)
n2=prime(2)
n3=prime(6)