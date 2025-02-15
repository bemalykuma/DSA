import json

def insertSort(list, last):
    c = 1
    count_in, count_out = 0, 0
    while last:
        hold = c
        walk = c - 1
        while walk >= 0 and list[hold] < list[walk]:
            if list[hold][0] == list[walk][0]:
                if int(list[hold][1:]) < int(list[walk][1:]):
                    list.insert(walk+1, list.pop(walk))
                else:
                    count_in -= 1
            else:
                list.insert(walk+1, list.pop(walk))
            hold -= 1
            walk -= 1
            count_in += 1
        if walk >= 0 and list[hold] > list[walk]:
            count_out += 1
        hold = walk + 1
        c += 1
        print(list)
        last -= 1
    print("Comparison times:", count_in + count_out)
    return

def main():
    l = json.loads(input())
    insertSort(l,int(input()))
main()