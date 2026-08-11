N = int(input())
C = list(map(int, input(). split()))

from collections import Counter
cnt = Counter(C)
print(N - cnt.most_common(1)[0][1])