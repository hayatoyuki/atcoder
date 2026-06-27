N, M = map(int, input().split())

A = []

for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

Todaycolor = []

for i in range(N):
    Todaycolor.append(A[i][0])

kind = []
Day = 1

while Day <= M:
    for j in range(N):
        if A[j][1] <= Day:
            Todaycolor[j] = A[j][2]
    kind.append(len(set(Todaycolor)))
    Day += 1

for x in kind:
    print(x)