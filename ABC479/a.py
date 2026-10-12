N = int(input())
A = list(map(int, input().split()))
total = sum(A[::2])

print(total)