#This program calculates the average and total marks of 3 student

class student:
    def __init__(self):
        self.name=input("name :")
        self.m1=int(input("m1 :"))
        self.m2=int(input("m2 :"))
        self.m3=int(input("m3 :"))
           
    def total(self):
        print("The total of ",self.name, "is", self.m1+self.m2+self.m3)
        
    def avg(self):
        print("The average of ",self.name,"is", (self.m1+self.m2+self.m3) / 3)
     
p1=student()
p2=student()
p3=student()

p1.avg()
p2.avg()
p3.avg()

p1.total()
p2.total()
p3.total()
    