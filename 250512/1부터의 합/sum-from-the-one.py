N = int(input())
calc = 0
for i in range(1,101):
    calc += i
    if calc >= N:
        print(i)
        break

    