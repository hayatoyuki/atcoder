N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

counter = [0] * N
count = 0

for t in T:
    if t in S:
        counter[S.index(t)] += 1
        continue

    candidates = []
    for j in range(N):
        s = S[j]
        if len(t) == len(s):
            diff_count = sum(a != b for a, b in zip(t, s))
            if diff_count == 1:
                candidates.append(j)

    if len(candidates) == 1:
        counter[candidates[0]] += 1

print(*counter)