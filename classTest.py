class Student(object):
    def __init__(self,name,course,grade, marks):
        self.name = name
        self.course = course
        self.grade = grade
        self.marks = marks
    def marking(self):
        if(int(self.marks)<50):
            print("fail")
        else:
            print("pass")


abi = Student("abi", "science", "9", "100")
print(abi.name)
print(abi.course)
print(abi.grade)
print(abi.marks)
abi.marking()