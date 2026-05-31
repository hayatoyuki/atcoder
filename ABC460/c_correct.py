N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

ans = 0
i = 0

for b in B:
    while i < N and b > 2 * A[i]:
        i += 1

    if i < N:
        ans += 1
        i += 1

print(ans)
