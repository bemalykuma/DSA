class Student:
    def __init__(self, name, sx, age, student_id, gpa):
        self.name = name
        self.sx = sx
        self.age = age
        self.student_id = student_id
        self.gpa = f"{gpa:.2f}"
    
    def student(self):
        if self.sx == "Male":
          self.sx = "Mr"
        elif self.sx == "Female":
          self.sx = "Miss"
        return f"{self.sx} {self.name} ({self.age}) ID: {self.student_id} GPA {self.gpa}"
    
first = Student(input(), input(), input(), input(), float(input()))
second = Student(input(), input(), input(), input(), float(input()))
third = Student(input(), input(), input(), input(), float(input()))
search_id = input()
if search_id in first.student():
  print(first.student())
elif search_id in second.student():
  print(second.student())
elif search_id in third.student():
  print(third.student())
else:
  print("Student not found")
  