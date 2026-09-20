from bisect import bisect_right

N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 安い順
A.sort()
B.sort()

# B[i]を買うために必要なKドル紙幣の枚数
BK = []
for b in B:
    BK.append((b + K - 1) // K)

# 累積和
AC = [0]
for a in A:
    AC.append(AC[-1] + a)

BC = [0]
for b in B:
    BC.append(BC[-1] + b)

BKC = [0]
for bk in BK:
    BKC.append(BKC[-1] + bk)

ans = 0

# 安いドリンクをri個買う場合をすべて試す
for ri in range(M + 1):

    # ドリンク購入後に残る総金額
    s = X + K * Y - BC[ri]

    # ドリンク購入に必要なKドル紙幣を引いた残り
    sk = Y - BKC[ri]

    # この個数のドリンクはそもそも買えない
    if s < 0 or sk < 0:
        break

    # 残金sで安いデザートを何個買えるか
    li = bisect_right(AC, s) - 1

    ans = max(ans, ri + li)

print(ans)