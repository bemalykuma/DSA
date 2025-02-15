def Sort(list, last):
    c = 1
    while last:
        hold = c
        walk = c - 1
        while walk >= 0 and list[hold] < list[walk]:
            list.insert(walk+1, list.pop(walk))
            hold -= 1
            walk -= 1
        hold = walk + 1
        c += 1
        last -= 1
    return list

def main(n):
    for _ in range(n):
        lis_sum, lis_point, lis_result = [], [], []
        for _ in range(int(input())):
            point = input().split()
            lis_sum.append(int(point[0])+int(point[1]))
            lis_point.append((int(point[0])+int(point[1]), int(point[0]), int(point[1])))
        sxrted = Sort(lis_sum, len(lis_sum)-1)

        count = 0
        for i in range(len(lis_point)):
            lis_same_y, lis_y = [], []
            for j in range(len(lis_point)):
                if sxrted[i] == lis_point[j][0] and count == 0:
                    re = lis_point[j][1], lis_point[j][2]
                    count += 1
                if sxrted[i] == lis_point[j][0] and count > 0:
                    lis_y.append(lis_point[j][2])
                    lis_same_y.append(lis_point[j])
            if count > 0:
                sxrt_y = Sort(lis_y, len(lis_y)-1)
                sxrt_y.reverse()
                for m in range(len(sxrt_y)):
                    for j in range(len(sxrt_y)):
                        if sxrt_y[m] == lis_same_y[j][2]:
                            re = lis_same_y[j]
                    if not re in lis_result:
                        lis_result.append(re)
            else:
                lis_result.append(re)
            if len(lis_result) == len(lis_point):
                break

        for i in lis_result:
            print(i[1], i[2])

main(int(input()))