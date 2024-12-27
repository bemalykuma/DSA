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

def infix_to_postfix(text): 
    operation = ArrayStack()
    result = ""
    text = text.replace(" ","")
    for i in text:
        if not i in "+-*/":
            result += i
        else:
            if operation.is_empty():
                operation.push(i)
            else:
                if operation.get_stack_top() in "+-" and i in "*/":
                    operation.push(i)
                elif (operation.get_stack_top() in "*/" and i in "*/") or (operation.get_stack_top() in "+-*/" and i in "+-"):
                    while operation.is_empty() is False:
                        x = operation.pop()
                        result += x
                    operation.push(i)
    while operation.is_empty() is False:
        x = operation.pop()
        result += x
    print(result)
infix_to_postfix(input())
