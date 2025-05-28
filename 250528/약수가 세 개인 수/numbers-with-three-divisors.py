start, end = map(int, input().split())
ss = 0
# Please write your code here.
for i in range(start,end+1):
    count = 0
    for x in range(1,i+1):
        if i % x == 0:
            count += 1
    if count == 3:
        ss += 1
print(ss)
                
            