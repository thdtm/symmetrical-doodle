A, B = map(int,input().split())
nums = []
for i in range(A,B+1):
    if i % 2 == 0:
        nums.append(i)
print(f'{sum(nums)}')
    