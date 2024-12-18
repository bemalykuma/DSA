from stack import ArrayStack

# รับค่า
stack = ArrayStack()
while True:
    x = input()
    if x == "-1":
        break
    stack.push(x)
stack.print_stack()