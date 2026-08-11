import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = [0] * N
idxs = []
ans = 0

for _ in range(Q):
    B = list(map(int, input().split()))

    if B[0] == 1:
        x = B[1] - 1
        if A[x] == 0:
            idxs.append(x)
        ans ^= A[x] ^ (A[x] + 1)
        A[x] += 1
    else:
        for k in idxs:
            ans ^= A[k] ^ (A[k] - 1)
            A[k] -= 1
        idxs = [k for k in idxs if A[k] != 0]

    print(ans)
