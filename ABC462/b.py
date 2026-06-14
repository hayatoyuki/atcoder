N = int(input())

K = []
A = []
B = []

for i in range(N):
    row = list(map(int, input().split()))

    K.append(row[0])
    A.append(row[1:])

B = [[] for _ in range(N)]

for n in range(len(A)):
    for j in A[n]:
        B[j - 1].append(n + 1)

for row in B:
    row.sort()

for m in range(N):
    B[m].insert(0, len(B[m]))

for row in B:
    print(*row)