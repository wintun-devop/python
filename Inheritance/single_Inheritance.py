
class Person:
    def __init__(self,first_name,last_name):
        self.fname=first_name
        self.lname=last_name
    def get_name_output(self):
        # print(f"{self.fname} {self.lname}")
        return f"{self.fname} {self.lname}"

class Student(Person):
    def __init__(self,first_name,last_name,id,class_id):
        super().__init__(first_name,last_name)
        self.id=id
        self.class_id=class_id
        
    def get_student_info(self):
        return f"The student name is {self.fname} {self.lname}.student id is {self.id}.Class is {self.class_id}."
        
    
wintun = Student("Win","Tun","123","cl123")
# print(wintun.get_name_output())
print(wintun.get_student_info())