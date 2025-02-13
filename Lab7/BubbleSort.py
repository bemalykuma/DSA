import json
def bubbleSort(list, last):
    c, count = 0, 0
    sxrted = False
    while c <= last and sxrted is False:
        walker = last
        sxrted = True
        while walker > c:
            if list[walker] < list[walker - 1]:
                sxrted = False
                list.insert(walker, list.pop(walker-1))
            walker -= 1
            count += 1
        c += 1
    print(list)
    print("Comparison times:", count)
    return

def main():
    l = json.loads(input())
    bubbleSort(l,int(input()))
main()
