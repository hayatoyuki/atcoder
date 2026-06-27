H, W = map(int, input().split())

A = []

for _ in range(H):
    row = list(input())
    A.append(row)

while A and "#" not in A[0]:
    A.pop(0)
while A and "#" not in A[-1]:
    A.pop()

B = []

for col in zip(*A):
    B.append(list(col))

while B and "#" not in B[0]:
    B.pop(0)
while B and "#" not in B[-1]:
    B.pop()
    
for row in zip(*B):
    print("".join(row))