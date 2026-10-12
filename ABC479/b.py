N = int(input())
S = input()

count = 0
log = []

for i in range(N):
    if S[i] == "R":
        count += 1
    else: 
        log.append(count)
        count = 0
log.append(count)

print(max(log))