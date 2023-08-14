class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_age(self):
        return f"My age is {self.age}"

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def get_full_name(self):
        return f"{super().get_full_name()} (Student ID: {self.student_id})"

class Teacher(Person):
    def __init__(self, first_name, last_name, age, employee_id):
        super().__init__(first_name, last_name, age)
        self.employee_id = employee_id

    def teach(self):
        return f"{self.get_full_name()} is giving a lesson."

person1 = Person("Ivan", "Bogun", 55)
print(person1.get_full_name())
print(person1.get_age())

teacher1 = Teacher('Roman', 'Smyk', 24, 1)
print(teacher1.get_full_name())
print(teacher1.get_age())
print(teacher1.teach())

student1 = Student('Dmitro', 'Kishinsky', 25, 1)
print(student1.get_full_name())
print(student1.get_age())

student2 = Student('Oleh', 'Saparin', 31, 2)
print(student2.get_full_name())
print(student2.get_age())
