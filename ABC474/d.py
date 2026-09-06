N = int(input())
A = list(map(int, input(). split()))
B = list(map(int, input(). split()))

W = []
ans = 0

for i in range(N):
    diff = A[i] - B[i]

    if diff > 0:
        w = 10**18
    else:
        w = 1

    W.append(w)
    ans += diff * w

if ans > 0:
    print("Yes")
    print(*W) # *answer は、リストの中身を「要素ごとに展開して」渡す記号
                # 出力形式で、角括弧なし・空白区切りで表示したいときに使う
else:
    print("No")