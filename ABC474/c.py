N, Q = map(int, input(). split())
P = list(map(int, input(). split()))
a = [int(input()) for _ in range(Q)]

for n in range(N):
    for i in range(Q):
        if P[n] == a[i]:
            P.remove(a[i])
            P.append(a[i])

print(P)

# TLEのため不正解