from collections import deque

h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

r = [0] * h
c = [0] * w
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            r[i] = 1
            c[j] = 1

d = [[-1] * w for i in range(h)]
q = deque()
for i in range(h):
    for j in range(w):
        if r[i] == c[j] == 0:
            d[i][j] = 0
            q.append((i, j))

ans = 0
while q:
    i, j = q.popleft()
    if d[i][j] <= k:
        ans += 1
    for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        if 0 <= ni < h and 0 <= nj < w:
            if s[ni][nj] == "." and d[ni][nj] == -1:
                d[ni][nj] = d[i][j] + 1
                q.append((ni, nj))

print(ans)
