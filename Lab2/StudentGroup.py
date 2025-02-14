class ArrayStack():
    def __init__(self) :
        self.size = 0
        self.data = list()
    def push(self, input_data) :
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self) :
        if self.data == list():
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            self.size -= 1
            x = self.data.pop()
            return x

    def is_empty(self) :
        if self.data == list():
            return True
        else:
            return False
        

    def get_stack_top(self) :
        if self.data == list():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            x = self.data.copy()
            result = x.pop()
            return result

    def get_size(self) :
        return self.size

    def print_stack(self) :
        print(self.data)
    
#Student

def student_group(group, num):
    student = ArrayStack()
    all_list = list()
    count = 0
    for _ in range(num):
        student.push(input())

    for _ in range(group):
        n_list = list()
        all_list.append(n_list)
    while not student.is_empty():
        for i in all_list:
            if student.is_empty():
                break
            x = student.pop()
            i.append(x)
    for i in all_list:
        count += 1
        temp = ""
        for j in i:
            temp += ", " + j
        temp = temp.replace(", ","",1)
        print(f"Group {count}: {temp}")
student_group(int(input()), int(input()))