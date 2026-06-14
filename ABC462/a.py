S = input()
numbers = ""

for c in S:
    if c.isdigit():
        numbers += c

print(numbers)