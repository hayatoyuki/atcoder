from bisect import bisect_right

N = int(input())

stack = []

for _ in range(N):
    h, l = map(int, input().split())

    while stack and stack[-1][0] <= h:
        stack.pop()

    stack.append((h, l))

H = []
L = []

for h, l in stack:
    H.append(h)
    L.append(l)

Q = int(input())
T = list(map(int, input().split()))

for t in T:
    idx = bisect_right(L, t)
    print(H[idx])