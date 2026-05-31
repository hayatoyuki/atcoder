s = "HelloWorld"

index = int(input("削除したい位置"))

if 1 <= index <=10:
    result = s[:index-1] + s[index:]
    print(result)
else: 
    print("1以上10 以下の整数を入力してください")