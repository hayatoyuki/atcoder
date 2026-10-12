from itertools import combinations

N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
A = [a for a, b in items]
B = [b for a, b in items]

result = []
oisisa = []

for k in range(1, N + 1):
    for indexes in combinations(range(N), k):
        if sum(B[i] for i in indexes) <= W:
            result.append(indexes)
            oisisa.append(sum(A[i] for i in indexes))

print(max(oisisa, default=0))