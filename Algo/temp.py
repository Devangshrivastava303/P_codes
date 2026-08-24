class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
            print(self.name,sum/3)
s1=Student("devang",[100,100,100])
s1.avg()