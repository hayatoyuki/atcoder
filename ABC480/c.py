N, K, T = map(int, input().split())
A = list(map(int, input().split()))

nowater = [1]*T

for i in range(N):
    nowater[A[i]-1:A[i]+K-1] = [0] * K
