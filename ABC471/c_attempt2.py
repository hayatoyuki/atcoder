from collections import deque

N = int(input())
A = list(map(int, input().split()))

location = 0
counter = 0
positive = []
negative = []

for a in A:
    if a > 0:
        positive.append(a)
    else:
        negative.append(a)

positive.sort()
negative.sort(reverse=True)

positive = deque(positive)
negative = deque(negative)


while positive or negative:
    if positive and negative:
        if abs(positive[0] - location) < abs(negative[0] - location):
            nearest = positive.popleft()
          
        else:
            nearest = negative.popleft()

    elif positive:
        nearest = positive.popleft()

    else:
        nearest = negative.popleft()

    counter += abs(nearest - location)
    location = nearest

print(counter)