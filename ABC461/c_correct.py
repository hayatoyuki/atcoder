from collections import defaultdict

N, K, M = map(int, input().split())

gems = defaultdict(list)

for _ in range(N):
    C, V = map(int, input().split())
    gems[C].append(V)

first = []
rest = []

for color in gems:
    gems[color].sort(reverse=True)

    # この色から最低1個選ぶ候補
    first.append(gems[color][0])

    # 同じ色の2個目以降は自由枠の候補
    for v in gems[color][1:]:
        rest.append(v)

first.sort(reverse=True)
rest.sort(reverse=True)

ans = 0

# M種類の色を確保
ans += sum(first[:M])

# 使わなかった「各色の最大値」も自由枠に入れられる
for v in first[M:]:
    rest.append(v)

rest.sort(reverse=True)

# 残り K-M 個を選ぶ
ans += sum(rest[:K - M])

print(ans)