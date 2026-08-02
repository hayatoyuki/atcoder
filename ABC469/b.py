N = int(input())
S = input()

count = 0

if N == 1:
    if S[0] == "x":
        count += 1

else:
    for i in range(N):

        if i == 0:
            if S[i] == "x" and S[i + 1] == "x":
                count += 1
                
        elif i == N - 1:
            if S[i - 1] == "x" and S[i] == "x":
                count += 1

        else:
            if S[i - 1] == "x" and S[i] == "x" and S[i + 1] == "x":
                count += 1

print(count)
