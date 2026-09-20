N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
x = X
y = Y
A.sort()
B.sort()
count = 0

for n in range(M):
    if B[n] <= K*Y:
        if B[n] != K*Y:
            Y -= ((B[n] // K) + 1)
            X += K - (B[n] % K)
        else:
            Y -= B[n] // K
        count += 1
    else:
        break

for m in range(N):
    if Y > 0:
        if A[m] <= K*Y:
            if A[m] != K*Y:
                Y -= ((A[m] // K) + 1)
                X += K - (A[m] % K)
            else:
                Y -= A[m] // K
        else:
            if A[m] - K*Y <= X:
                X -= A[m] - K*Y 
                Y = 0
            else:
                break
        count += 1

    else:
        if A[m] <= X:
            X -= A[m]
            count += 1
        else:
            break
print(count)