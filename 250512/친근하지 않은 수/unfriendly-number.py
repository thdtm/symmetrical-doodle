N = int(input())
count = N
for i in range(1,N+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        count -= 1
print(count)
        