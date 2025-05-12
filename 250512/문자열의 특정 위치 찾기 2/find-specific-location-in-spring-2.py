fuck = ['apple','banana','grape','blueberry','orange']
user = input()
count = 0
arr = []
for i in fuck:
    if i[2] == user or i[3] == user:
        count += 1
        arr.append(i)
for i in arr:
    print(i)
print(count)

    