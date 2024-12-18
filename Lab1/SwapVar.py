def string_to_tuple(text):
    ans = text.strip('()').split(',')
    return tuple(map(float, ans))

def swap():
    temp = string_to_tuple(input())
    x = temp[0]
    y = temp[1]
    print(f"({y}, {x})")
swap()
