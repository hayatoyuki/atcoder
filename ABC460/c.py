N, M = map(int, input().split())
A = []
for x in A:
    row = list(map(int, input().split()))
    row.sort(reverse=True)
    A.append(row)

L = list(map(int, input().split()))

A = []

for x in L:
    row = list(map(int, input().split()))
    row.sort(reverse=True)
    A.append(row)

for row in A:
    print(*row)