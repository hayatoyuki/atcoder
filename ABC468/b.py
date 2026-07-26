M, D = map(int, input().split())
S = input()

A = [0] * M

for i in range(M):
    if S[i] == "G":
        for j in range(max(0, i - D), min(len(A), i + D + 1)):
            A[j] += 1

print(A.count(0))