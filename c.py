N, Q = map(int, input().split())
A = [0] * N
for _ in range(Q):

    query = list(map(int, input().split()))

    if query[0] == 1:
        A[query[1]] += 1

    else:
        query[1] = int(input())
        count = 0
        for x in A:
            if x >= query[1]:
                count += 1
    print(count)
