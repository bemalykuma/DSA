from stack import ArrayStack

def is_parentheses_matching(expression):
    open = ArrayStack()
    close = ArrayStack()
    for i in expression:
        if i == "(":
            open.push("(")
        elif i == ")":
            close.push(")")
    if open.get_size() == close.get_size():
        return True
    else:
        return False

# Test
# str = "((A-B)*C))("
# result = is_parentheses_matching(str)
# print(result)
