n = int(input())
for _ in range(n):
    num = 0
    a, b = map(int,input().split())
    for i in range(a,b+1):
        if i % 2 == 0:
            num += i
    print(num)
             