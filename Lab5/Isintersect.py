def isIntersect(a,b,c):
    for i in range(len(a)):
        if a[i] in b and a[i] in c:
            return True
    return False

def main():
    a = input().strip("[").strip("]").split(", ")
    b = input().strip("[").strip("]").split(", ")
    c = input().strip("[").strip("]").split(", ")
    print(isIntersect(a,b,c))
main()