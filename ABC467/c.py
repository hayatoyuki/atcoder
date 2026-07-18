N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count0 = 0
count1 = 1

A0 = A[:]
B0 = B[:]

A1 = A[:]
B1 = B[:]
A1[0] += 1

for i in range(N - 1):
    while (A0[i] + A0[i + 1]) % M != B0[i]:
        A0[i + 1] += 1
        count0 += 1


for i in range(N - 1):
    while (A1[i] + A1[i + 1]) % M != B1[i]:
        A1[i + 1] += 1
        count1 += 1

if count0 > count1:
    print(count1)
else:
    print(count0)
