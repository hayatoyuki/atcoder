N, M = map(int, input().split())

count = 0
# M の値が 0 でない間以下の操作を繰り返す
while M != 0: 
    r = N % M
    M = r
    count += 1

print(count) 
