'''Calculator'''
def calculator(n):
    if n == 1:
        return 1
    temp = 0
    for i in range(1 , n+1):
        temp += len(str(i))+1
    return temp
    # return sum(len(str(i)) + 1 for i in range(1, n+1))

print(calculator(int(input())))