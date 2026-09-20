N = int(input())
S = input()
T = input()

if all(S[n] == T[n] or T[n] == "*" for n in range(N)):
    print("Yes")
else:
    print("No")