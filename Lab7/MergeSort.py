import json

def mergeSort(list):
    if len(list) <= 1:
        return list
    else:
        middle = len(list)//2
        left = list[:len(list)-middle]
        right = list[len(list)-middle:]
        left = mergeSort(left)
        right = mergeSort(right)
        result = merge(left, right)
        return result

def merge(left, right):
    result = []
    count = 0
    if not len(left):
        return right
    if not len(right):
        return left
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        count += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    print(count)
    return result

def main():
    l = json.loads(input())
    print(mergeSort(l))
main()