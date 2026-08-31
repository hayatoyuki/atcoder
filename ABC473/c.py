from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = Counter(A)

counts = sorted(set(cnt.values()), reverse=True)

if len(counts) < 2:
    top_counts = [counts[0]]
else:
    first = counts[0]
    second = counts[1]

    if first - second > 1:
        top_counts = [counts[0]]
    else:
        top_counts = counts[:2]
ans = []

for x, c in cnt.items():
    if c in top_counts:
        ans.append(x)

print(len(ans))