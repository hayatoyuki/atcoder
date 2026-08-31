N = int(input())
A = list(map(int, input().split()))

ans = sum(A[N//2:N])
print(ans)