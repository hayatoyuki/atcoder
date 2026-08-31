N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
X = []
ans = 0

for n in range(N):
    ans += A[n]*(n + 1)

    if ans == K:
        count += 1
        X.append(A)