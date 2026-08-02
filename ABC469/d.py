N, M = map(int, input().split())

pairs = []

for _ in range(M):
    a, b = map(int, input().split())
    pairs.append((a, b))

u, v = pairs[0]

def count_with(p):
    need = 0
    cnt = [0] * (N + 1)

    for a, b in pairs:
        if a == p or b == p:
            continue

        need += 1
        cnt[a] += 1
        cnt[b] += 1

    if need == 0:
        return N - 1

    res = 0
    for q in range(1, N + 1):
        if q != p and cnt[q] == need:
            res += 1

    return res

ans = count_with(u) + count_with(v)

ok_uv = True
for a, b in pairs:
    if a != u and b != u and a != v and b != v:
        ok_uv = False

if ok_uv:
    ans -= 1

print(ans)