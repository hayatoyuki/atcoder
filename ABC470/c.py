N, Q = map(int, input(). split())
A = [0] * N
B = []

for _ in range(Q):
    B.append(list(map(int, input().split())))

for i in range(Q):

    if B[i][0] == 1:
        A[B[i][1] - 1] += 1
    else:
        for k in range(N):
            if A[k] >= 1:
                A[k] -= 1

    ans = 0

    for j in range(N):
        ans ^= A[j]
        
    print(ans)

    
