# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금
# 같은 눈이 2개만 나오는 경우 에는 1,000원+(같은 눈)×100원의 상금
# 모두 다른 눈이 나오는 경우 에는 (그 중 가장 큰 눈)×100원의 상금
# 상금 출력

a, b, c = map(int, input().split())

if a == b == c:
    print(a * 1000 + 10000)
elif a == b or b == c or a == c:
    if a == b or a == c:
        print(a * 100 + 1000)
    else:
        print(b * 100 + 1000)
else:
    print(max(a, b, c) * 100)

