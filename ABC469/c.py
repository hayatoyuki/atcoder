N = int(input())
S = input()

prefix = [0] * (N + 1)

for i in range(N):
    if S[i] == "o":
        prefix[i + 1] = prefix[i] + 1
    else:
        prefix[i + 1] = prefix[i]

output = []

cantake = 0
taked = 0

for i in range(1, N + 1):

    cantake = prefix[i]
    taked = i

    while cantake > 0 and taked < N:
        now = cantake
        cantake = prefix[min(taked + now, N)] - prefix[taked]
        taked += now
        
    output.append(min(taked, N))
    cantake = 0
    taked = 0

print(*output, sep="\n")