class Student:
    def __init__(self,name,rollno,course,fees):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.fees=fees
    def display(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno) 
        print("Course:",self.course)
        print("Fees:",self.fees)
