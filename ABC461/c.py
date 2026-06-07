N, K, M = map(int, input().split())
items = []
for _ in range(N):
    a, b = map(int, input().split())
    items.append((b, a))
items.sort(reverse=True)
selected = items[:K]