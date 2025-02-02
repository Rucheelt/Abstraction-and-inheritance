class student(object):
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("Name:",self.name)
        print("rollno:",self.rollno)

class rucheel(student):
    def __init__(self,name,rollno,grade,section):
        self.grade=grade
        self.section=section

        super().__init__(name,rollno)
    
s=rucheel("Rucheel","7117","12","India")
s.display()