N = int(input())
count = 0
j = 2

for i in range(1, N+1):

    if j <= i:
        j = i + 1

    while j <= N:
        print("?", i, j, flush=True)
        res = input()

        if res == "Yes":
            j += 1
        else:
            break  
    count += j - i - 1
print("!", count, flush=True)