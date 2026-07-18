H, W = map(int, input().split())
BMI = W / H / H * 10000

if  BMI >= 25:
    print("Yes")
else:
    print("No")