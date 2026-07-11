N, M = map(int, input().split())
MAX = [-1] * M

for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    if b > MAX[a]:
        MAX[a] = b

print(*MAX)