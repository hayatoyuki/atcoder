import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

L = [0] + [0] + list(map(int, input().split()))  # L[2] から L[N]
R = [0] + list(map(int, input().split()))        # R[1] から R[N-1]
# マス番号とPythonのインデックスを一致させるために、先頭へ0を追加している。
# L = [0, 0, 6, 2, 20, 9, 1]
# R = [0, 1, 12, 9, 5, 2]

# R_1 ... R_i の最小値
prefix_R = [0] * (N + 1)
prefix_R[1] = R[1]
for i in range(2, N):
    prefix_R[i] = min(prefix_R[i - 1], R[i])

# L_i ... L_N の最小値
suffix_L = [0] * (N + 2)
suffix_L[N] = L[N]
for i in range(N - 1, 1, -1):
    suffix_L[i] = min(L[i], suffix_L[i + 1])

for _ in range(Q):
    s, t = map(int, input().split())

    if s < t:
        answer = R[s]
        if s > 1:
            answer = min(answer, L[s] + prefix_R[s - 1])
    else:
        answer = L[s]
        if s < N:
            answer = min(answer, R[s] + suffix_L[s + 1])

    print(answer)