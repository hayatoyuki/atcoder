N = int(input())
words = input().split()

ans = ""

if 1 <= N <= 10:
    for s in words:
        if 1 <= len(s) <= 10:
            if s[0] in "abc":
                ans += "2"
            elif s[0] in "def":
                ans += "3"
            elif s[0] in "ghi":
                ans += "4"
            elif s[0] in "jkl":
                ans += "5"
            elif s[0] in "mno":
                ans += "6"
            elif s[0] in "pqrs":
                ans += "7"
            elif s[0] in "tuv":
                ans += "8"
            else:
                ans += "9"

print(ans)