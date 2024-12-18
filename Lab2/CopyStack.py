from stack import ArrayStack

def copyStack(stack1, stack2):
    stack_temp = ArrayStack()
    while True:
        if stack2.is_empty():
            break
        stack2.pop()
    while True:
        if stack1.is_empty():
            break
        x = stack1.pop()
        stack_temp.push(x)
    while True:
        if stack_temp.is_empty():
            break
        x = stack_temp.pop()
        stack1.push(x)
        stack2.push(x)

# test
# s1 = ArrayStack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s2 = ArrayStack()
# s2.push(80)
# s2.push(90)
# s1.print_stack()
# s2.print_stack()
# copyStack(s1, s2)
# s1.print_stack()
# s2.print_stack()