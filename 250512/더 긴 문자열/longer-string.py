a, b = input().split()
if len(a) == len(b):
    print('same')
if len(a) > len(b):
    print(f'{a} {len(a)}')
elif len(b) > len(a):
    print(f'{b} {len(b)}')