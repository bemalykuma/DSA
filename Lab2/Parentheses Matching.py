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
    
#is_parenthese_matching
def is_parentheses_matching(expression):
    o = ArrayStack()
    size = 0
    for i in expression:
        if i == "(":
            o.push("(")
            size += 1
        elif i == ")":
            o.pop()
            size -= 1
    if size < 0 :
        return False
    if o.is_empty():
        return True
    else:
        return False

def main(sam):
    result = is_parentheses_matching(sam)
    if result is True:
        print("Parentheses in " + sam + " are matched")
    else:
        print("Parentheses in " + sam + " are unmatched")
    print(result)
main(input())
