arr = []
A, B = map(int, input().split())
arr.append(A)
while A < B:
    if A % 2 == 0:
        A += 3
        arr.append(A)
        if A > B:
            arr.pop(-1)
    else:
        A *= 2
        arr.append(A)
        if A > B:
            arr.pop(-1)
print(*arr)
