N = int(input())
nums = list(map(int,input().split()))
square = [x**2 for x in nums]
print(*square)