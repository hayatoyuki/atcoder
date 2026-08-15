from collections import Counter

N = int(input())
strings = [input() for _ in range(N)]

counts = Counter(s.lower() for s in strings)
answer = max(counts.values())

print(answer)