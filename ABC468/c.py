N = int(input())
P = input().split()
Q = input().split()

P_str = "".join(P)
Q_str = "".join(Q)

P_NUM = int(P_str, N)
Q_NUM = int(Q_str, N)

if P_NUM > Q_NUM:
    print(0)
else:
    print(Q_NUM - P_NUM)