N, Q = map(int, input(). split())
P = list(map(int, input(). split()))
a = [int(input()) for _ in range(Q)]

seen = set()
moved = []

for x in reversed(a):
    if x not in seen:
        seen.add(x)
        moved.append(x)

moved.reverse()

answer = [x for x in P if x not in seen] + moved

print(*answer)