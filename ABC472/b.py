N = int(input())
L = list(map(int, input().split()))

ans = []*N

for n in range(N):
    left = sum(L[:n-1])
    right = sum(L[n-1:])
    ans.append(abs(right - left))

print(min(ans))