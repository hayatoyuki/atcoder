T = int(input())
A = []
for _ in range(T):
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split())

    if (X2 - X1)**2 + (Y2 - Y1)**2 <= (R1 + R2)**2 and (X2 - X1)**2 + (Y2 - Y1)**2 >= (R1 - R2)**2:
        print("Yes")
    else:
        print("No")


