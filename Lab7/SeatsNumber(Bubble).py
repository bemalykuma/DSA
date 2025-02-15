import json
def bubbleSort(list, last):
    c, count = 0, 0
    sxrted = False
    while c <= last and sxrted is False:
        walker = last
        sxrted = True
        while walker > c:
            if list[walker][0] == list[walker-1][0]:
                if int(list[walker][1:]) < int(list[walker-1][1:]):
                    sxrted = False
                    list[walker], list[walker-1] = list[walker-1], list[walker]
            elif list[walker] < list[walker - 1]:
                sxrted = False
                list[walker], list[walker-1] = list[walker-1], list[walker]
            walker -= 1
            count += 1
        print(list)
        c += 1
    print("Comparison times:", count)
    return

def main():
    l = json.loads(input())
    bubbleSort(l,int(input()))
main()
