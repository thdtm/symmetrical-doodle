N = int(input())
nums = list(map(int, input().split()))
calc = []
for i in nums:
    if i % 2 == 0:
        calc.append(i)
for a in range(-1, -len(calc)-1,-1):
    print(calc[a],end=' ')

