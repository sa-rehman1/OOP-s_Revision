#Initiate a class
class Employee:
    #Special method / dunder method -- Constructor

    def __init__(self):
        self.id=123
        self.salary=50000
        self.designation="SDE"


    #Creating a method

    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")

#Creating an instance of a class
sam=Employee()

print(sam.salary)

sam.travel("Hyderabad")
