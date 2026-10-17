N, K, T = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
end = 0  # ここまで連続してお湯が出るようにした時刻

for a in A:
    if a >= T:
        break

    # 次に青木君が押すまでの不足分を埋める
    if end < a:
        d = a - end
        ans += (d + K - 1) // K 
        #dをKで割って小数点以下を切り上げるための書き方

    # 青木君が押すと、時刻 a + K までお湯が出る
    end = max(end, a + K)

# 最後に時刻 T までの不足分を埋める
if end < T:
    d = T - end
    ans += (d + K - 1) // K

print(ans)