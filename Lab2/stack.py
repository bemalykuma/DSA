class ArrayStack():
    def __init__(self) :
        self.size = 0
        self.data = []
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
        if self.data == []:
            print("Underflow: Cannot pop data froman empty list")
            return None
        else:
            self.size -= 1
            x = self.data[-1]
            self.data.pop()
            return x

    def is_empty(self) :
        if self.data == []:
            return True
        else:
            return False
        

    def get_stack_top(self) :
        if self.data == []:
            print("Underflow: Cannot pop data froman empty list")
            return None
        else:
            return self.data[-1]

    def get_size(self) :
        return self.size

    def print_stack(self) :
        print(self.data)

# Test
# s1 = ArrayStack()
# s2 = ArrayStack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s2.push(15)
# s2.push(25)
# x = s1.pop()
# s2.push(x)
# x = s1.get_stack_top()
# s2.push(x)
# s1.print_stack()
# s2.print_stack()
# print(s2.is_empty())