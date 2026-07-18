N = int(input())

data = []
dif = 0

for _ in range(N):
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    data.append([A, B, C])

for i in range(N):
    if data[i][2] == "keep":
        dif += data[i][1] - data[i][0]

print(dif)