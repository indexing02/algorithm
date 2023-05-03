# 첫째 줄 부터 입력받은 n번째 줄까지 차례대로 별 출력
# 대신 첫째줄에 n-1개의 공백을 두고 점차 공백의 개수를 줄여가면서 출력

num = int(input())

for i in range(num):
    print(" " * (num - (i + 1)), end="")
    print("*" * (i + 1))
