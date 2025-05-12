score = int(input())
for _ in range(score,101):
    if score >= 90:
        print('A',end=' ')
        score += 1
    elif score >= 80:
        print('B',end=' ')
        score += 1
    elif score >= 70:
        print('C',end=' ')
        socre += 1
    elif score >= 60:
        print('D',end=' ')
        socre += 1
    else:
        print('F',end=' ')
        score += 1
    
