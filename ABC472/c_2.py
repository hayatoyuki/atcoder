N, M, K = map(int, input().split())
A = list(map(int, input().split()))

eat = 0

for n in range(N):
    eat += A[n]

    if n >= M:
        eat -= A[n - M]

    if eat <= K:
        print("Yes")
    else:
        eat -= A[n]
        A[n] = 0
        print("No")

        

    