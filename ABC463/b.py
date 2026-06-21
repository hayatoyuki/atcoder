N, X = input().split()
N = int(N)
Z = []

for _ in range(N):
    row = list(input())  # ○×○ のように入力
    Z.append(row)

j = ord(X) - ord("A")

for i in range(N):
    if Z[i][j] == "o":
        print("Yes")
        exit()

print("No")