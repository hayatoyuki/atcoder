import heapq

Q, V = map(int, input().split())

heap = []

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        _, t, w = query
        key = w - t     #　残量 = t+(w−t0​)なので、すべてのバッテリーに共通する t を無視すると、w - t0 が大きいバッテリーほど、現在の残量も大きい

        heapq.heappush(heap, -key)      
        # heapq で最大値を扱う基本テクニックとして、
        # heapq.heappush(heap, -x) 
        # x = -heapq.heappop(heap) 
        # という方法がある

    else:
        _, t = query

        if not heap:
            print(-1)   #heapが空の場合、-1を出力
        else:
            key = -heapq.heappop(heap)
            print(min(V, t + key))      #　初期残量 + 経過時間 　or　 最大容量V　の小さいほうを選択