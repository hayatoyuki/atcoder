from collections import deque
Q , V = map(int, input().split())
battery = []
queries = []

for _ in range(Q):
    queries.append(list(map(int, input().split())))
    
time = []

battery = deque(battery)
time = deque(time)

for i in range(Q):
    if queries[i][0] == 1:
        time.append(queries[i][1])
        battery.append(queries[i][2])
    else:
        

print()