def select(list, last):
    c = 0
    sxrted = []
    while len(sxrted) < last:
        small = c
        walker = c + 1
        while walker < len(list):
            if int(list[walker]) <= int(list[small]):
                small = walker
            walker += 1
        sxrted.append(list[small])
        list.pop(small)
    return sxrted

def main(n):
    for _ in range(n):
        lis_sum, lis_point, lis_y, lis_result, lis_x = [], [], [], [], []
        for _ in range(int(input())):
            temp = []
            point = input().split()
            lis_sum.append(int(point[0])+int(point[1]))
            temp.append(int(point[0])+int(point[1]))
            temp.append(int(point[0]))
            temp.append(int(point[1]))
            lis_point.append(temp)

        result = select(lis_sum, len(lis_sum))
        count = 0
        for i in range(len(lis_point)):
            for j in range(len(lis_point)):
                if result[i] == lis_point[j][0] and count == 0:
                    re = lis_point[j][1], lis_point[j][2]
                    count += 1
                if result[i] == lis_point[j][0] and count > 0:
                    lis_y.append(lis_point[j][2])
                    lis_x.append(lis_point[j])
            if count > 0:
                sxrt = select(lis_y, len(lis_y))
                sxrt.reverse()
                for m in range(len(sxrt)):
                    for j in range(len(sxrt)):
                        if sxrt[m] == lis_x[j][2]:
                            re = lis_x[j]
                    lis_result.append(re)
                lis_x, lis_y = [], []
            else:
                lis_result.append(re)
            if len(lis_result) == len(lis_point):
                break
        for i in lis_result:
            print(i[1], i[2])
main(int(input()))