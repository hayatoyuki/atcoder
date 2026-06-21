N = int(input())
A = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append((a, b))
   
A.sort(key=lambda x: x[1], reverse=True)
    
Q = int(input())
B = list(map(int, input().split()))

for i in range(Q):
    ans = -1

    for j in range(N):
        if A[j][1] > B[i]:
            ans = max(ans, A[j][0])
        else:
            break
    print(ans)