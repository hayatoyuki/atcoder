N = int(input())
A = list(map(int, input().split()))
A.sort()
location = 0
counter = 0

while A:
    nearest = min(A, key=lambda a: (abs(a - location), a))
    counter += abs(nearest - location)
    location = nearest
    A.remove(nearest)

print(counter)

#TLE