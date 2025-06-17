matrix1 = []
matrix2 = []
calc = []
for _ in range(3):
    a = list(map(int,input().split()))
    matrix1.append(a)

empty = input()

for _ in range(3):
    a = list(map(int, input().split()))
    matrix2.append(a)

for i in range(3):
    result = []
    for j in range(3):
        a = matrix1[i][j] * matrix2[i][j]
        result.append(a)
    calc.append(result)

for row in calc:
    print(*row)

