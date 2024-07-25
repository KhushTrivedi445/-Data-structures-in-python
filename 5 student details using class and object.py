#This programs gives the details of 5 students
class student:
    def __init__(self):
        self.name=input("name")
        self.roll_no=int(input("roll_no"))
        self.spi=int(input("spi"))
        self.branch=input("branch")
        
    def printdetails(self):
        print("The name is",self.name, ",roll_no is",self.roll_no,",spi is",self.spi,"and the branch is ",self.branch)
        
s1=student()
s2=student()
s3=student()
s4=student()
s5=student()

s1.printdetails()
s2.printdetails()
s3.printdetails()
s4.printdetails()
s5.printdetails()