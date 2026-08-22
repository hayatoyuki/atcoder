N, M, K = map(int, input().split())
A = list(map(int, input().split()))

for n in range(N):
    if sum(A[max(n-M+1, 0):n+1]) < K:
        print("Yes")
    else:
        A[n] = 0
        print("No")

        

    