import json
def selectSort(list, last):
    c, count = 0, 0
    a = last
    while last:
        small = c
        walker = c + 1
        while walker <= a:
            if list[small][0] == list[walker][0]:
                if int(list[small][1:]) > int(list[walker][1:]):
                    small = walker
            elif list[walker] < list[small]:
                small = walker
            walker += 1
            count += 1
        list[small], list[c] = list[c], list[small]
        c += 1
        last -= 1
        print(list)
    print("Comparison times:", count)
    return

def main():
    l = json.loads(input())
    selectSort(l,int(input()))
main()
