N = int(input())
A = list(map(int, input().split()))
log = sorted(A[:3], reverse=True)
print(log[2])

for x in A[3:]:
    if x > log[-1]:
        log[-1] = x
        log.sort(reverse=True)
    print(log[2])

