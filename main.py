class Human:
    def __init__(self, name="No name", surname="No surname", age="No age"):
        self.name = name
        self.surname = surname
        self.age = age
class Student:
    def __init__(self, scholarship="no scholarship"):
        self.human = human
        self.scholarship = scholarship

class Group:
    def __init__(self, namegroup="no namegroup"):
        self.namegroup = namegroup
        self.student = []

    def add_student(self, human):
        self.student.append(human)

    def group_details(self):
        if self.student != []:
            print(f"автобус {self.student} має пасажирів:")
            for student in self.student:
                print(student.name)

namegroup = Group("Champions")
namegroup.add_student(Human("Olga"))
namegroup.add_student(Human("Borys"))
namegroup.add_student(Human("Adolf"))
namegroup.add_student(Human("Yura"))
namegroup.add_student(Human("Oleg"))
namegroup.add_student(Human("Vovan"))
namegroup.group_details()


