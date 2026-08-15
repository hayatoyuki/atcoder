S = input()
T = input()

count = 0

for i in range(len(S)):
    if S[i] != T[i]:
        count += 1

if count == 1:
    print("Yes")
else:
    print("No")