from stack import ArrayStack

def is_parentheses_matching(expression):
    open = ArrayStack()
    for i in expression:
        if i == "(":
            open.push("(")
        elif i == ")":
            if open.is_empty():
                return False
            else:
                open.pop()
    if open.is_empty():
        return True
    else:
        return False

# Test
# str = "((A-B)*C)" //True  "((A-B)*C))(" //False
# result = is_parentheses_matching(str)
# print(result)
