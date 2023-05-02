# 시간을 입력받아 45분 일찍 출력하기

a, b = map(int, input().split())

if 0 > b - 45:
    if a == 0:
        a = 24
    a -= 1
    b = 60-(45-b)
    print(a, b)
else:
    print(a, b-45)
