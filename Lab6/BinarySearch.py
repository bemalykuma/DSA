import json

class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa
    
    def get_std_id(self):
        return self.std_id

    def get_name(self):
        return self.name

    def get_gpa(self):
        return self.gpa

    def print_details(self):
        print(f"ID: {self.std_id}")
        print("Name: " + self.name)
        print(f"GPA: {self.gpa:.2f}")

def binary_search(data, name):
    count = 0
    left = 0
    right = len(data) - 1
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if data[mid]["name"] == name:
            return mid, count
        elif data[mid]["name"] < name:
            left = mid + 1
        else:
            right = mid - 1
    return -1, count

def main():
    student = json.loads(input())
    name = input()
    position, Comparisons = binary_search(student, name)
    if position != -1:
        std = Student(student[position]["id"], student[position]["name"], student[position]["gpa"])
        print(f"Found {name} at index {position}")
        std.print_details()
        print(f"Comparisons times: {Comparisons}")
    else:
        print(f"{name} does not exists.")
        print(f"Comparisons times: {Comparisons}")
main()