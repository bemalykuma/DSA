import json
def selectSort(list, last):
    c, count = 0, 0
    a = last
    while last:
        small = c
        walker = c + 1
        while walker <= a:
            if int(list[walker]) < int(list[small]):
                small = walker
            walker += 1
            count += 1
        list.insert(c, list.pop(small))
        c += 1
        last -= 1
    print(list)
    print("Comparison times:", count)
    return

def main():
    l = json.loads(input())
    selectSort(l,int(input()))
main()
