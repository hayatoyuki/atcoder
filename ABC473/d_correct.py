N, K = map(int, input().split())

def dfs(i, s, A):
    if i == N - 1: # 最後の 1 項になったら
        if (K - s) % N == 0: # 合計を K にできるときのみ
            A[i] = (K - s) // N
            print(' '.join(str(a) for a in A)) # 出力
        return

    # i 項目を決めて再帰
    for x in range(0, (K - s) // (i + 1) + 1):
        A[i] = x
        dfs(i + 1, s + x * (i + 1), A)

dfs(0, 0, [0] * N)
