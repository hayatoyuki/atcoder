from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

perm = list(permutations(range(1, N + 1)))

p_index = perm.index(P)
q_index = perm.index(Q)

if p_index >= q_index:
    print(0)
else:
    print(q_index - p_index - 1)