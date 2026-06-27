from collections import defaultdict

N, M = map(int, input().split())

events = [[] for _ in range(M + 1)]
color_count = defaultdict(int)

for _ in range(N):
    a, b, c = map(int, input().split())

    color_count[a] += 1

    events[b].append((a, c))

for day in range(1, M + 1):
    for old_color, new_color in events[day]:
        color_count[old_color] -= 1

        if color_count[old_color] == 0:
            del color_count[old_color]

        color_count[new_color] += 1

    print(len(color_count))