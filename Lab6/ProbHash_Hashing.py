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

class ProbHash:
    def __init__(self, size):
        self.hash_table = list()
        self.size = size
        self.digit_list = list()
        self.digit_dict = {}
    
    def hash_func(self, key):
        digits = key % self.size
        while True:
            if not digits in self.digit_list:
                self.digit_list.append(digits)
                return digits
            else:
                digits = self.rehash(digits)
        
    def rehash(self, hkey):
        if hkey < self.size-1:
            return hkey + 1
        return hkey + 1 - self.size

    def insert_data(self, student):
        temp = []
        if len(self.hash_table) < self.size:
            index = self.hash_func(student.std_id)
            print(f"Insert {student.std_id} at index {index}")
            temp.append(student.std_id)
            temp.append(student.name)
            temp.append(student.gpa)
            self.hash_table.append(temp)
            self.digit_dict[student.std_id] = index
        else:
            print(f"The list is full. {student.std_id} could not be inserted.")

    def search_data(self, std_id):
        for i in self.hash_table:
            if std_id in i:
                print(f"Found {std_id} at index {self.digit_dict[std_id]}")
                return Student(i[0], i[1], i[2])
        print(f"{std_id} does not exist.")




def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()