N, Q = map(int, input().split())
L = list(map(int, input().split()))
R = list(map(int, input().split()))

items = [tuple(map(int, input().split())) for _ in range(Q)]
start= [a for a, b in items]
goal = [b for a, b in items]

for i in range(Q):
        if start[i] < goal[i]:
            for j in range(0, start[i] - 2):
                print(min(R[start[i] - 1], L[start[i] - 2] + R[j]))
        else:
            for k in range(start[i] - 1, N - 2):
                print(min(L[start[i] - 2], R[start[i] - 1] + L[k]))