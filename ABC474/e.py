import sys

input = sys.stdin.readline
for _ in range(int(input())): #range(int(input())) = range(T)
    N = int(input())
    base = 0
    minA = 10**9 #とりうる最大値を入れておく
    diff = []
    for _ in range(N):
        A, B = map(int, input().split())
        base += A
        minA = min(minA, A)
        diff.append(B - A)
    diff.sort()
    ans = base
    cur = base
    for k in range(1, N + 1):
        cur += diff[k - 1]
        ans = min(ans, cur + max(0, 2 * k - N) * minA) # N−k < kである場合 2k−N 枚クーポンが不足するため、新たに 2k−N 枚クーポンを購入する必要がある
    print(ans)
