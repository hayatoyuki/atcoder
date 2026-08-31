from collections import Counter
N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

B = []
for x, c in cnt.items():
    if c % 2 == 1:
        B.append(x)

print(sum(B))