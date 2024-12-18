import json
def spam(input):
    my_list = json.loads(input)
    mx, mn = 0, 0
    temp_mx = my_list[0]
    temp_mn = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > temp_mx:
            mx = my_list[i]
            temp_mx = mx
        else:
            mx = temp_mx
        if my_list[i] < temp_mn:
            mn = my_list[i]
            temp_mn = mn
        else:
            mn = temp_mn
    avg = sum(my_list) / len(my_list)
    print(f"({mx}, {mn}, {round(avg, 2)})")
spam(input())
