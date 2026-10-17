S = [input() for _ in range(2)]

if S[0][0] == 'A' and S[1][1] == 'D' or S[0][0] == 'D' and S[1][1] == 'A' or S[0][1] == 'A' and S[1][0] == 'D' or S[0][1] == 'D' and S[1][0] == 'A':
    print("No")
else:
    print("Yes")