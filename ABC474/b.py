N = int(input())
P = list(map(int, input(). split()))

l = 1
r = 10
x = 10

while l <= N:
    if any(value > x for value in P[l - 1:r]):
        print("No")
        break
    l += 10
    r += 10
    x += 10
else:
    print("Yes")