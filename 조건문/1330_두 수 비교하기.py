# 공백을 두고 두 자연수를 입력 받아
# A가 B보다 큰 경우 에는 '>'를 출력
# A가 B보다 작은 경우 에는 '<'를 출력
# A와 B가 같은 경우 에는 '=='를 출력

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
