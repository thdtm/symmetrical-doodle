m, n = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(m)]
matrix2 = [list(map(int, input().split())) for _ in range(m)]

result = []
for i in range(m):
    arr = []
    for j in range(n):
        if matrix1[i][j] == matrix2[i][j]:
            arr.append(0)
        else:
            arr.append(1)
    result.append(arr)

for row in result:
    print(*row)
