#finding factors using class and object
class factors:
    def __init__(self):
        self.num=int(input("Enter the number : "))
    def displayfactors(self):
        print("The factors of",self.num,"are")
        for i in range (1,self.num,1):
            if (self.num%i==0):
                print(i)
            
                

n1=factors()
n2=factors()
n3=factors()
n4=factors()
n5=factors()

n1.displayfactors()
n2.displayfactors()
n3.displayfactors()
n4.displayfactors()
n5.displayfactors()