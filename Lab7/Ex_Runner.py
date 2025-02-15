def Runner():
    s = int(input())
    lis, lis_time, lis_res = [], [], []
    for i in range(1, int(input())+1):
        point = input().split()
        v, amount_s, start = int(point[0]), (s-int(point[1])), int(point[1])
        time = amount_s/v
        lis_time.append((time, v, start))
        lis.append((v, start))
    minimum = min(lis_time)
    for i in lis_time:
        if minimum[0] == i[0]:
            lis_res.append((i[1],i[2]))
    max_v = max(lis_res)
    print(lis.index(max_v)+1)
Runner()