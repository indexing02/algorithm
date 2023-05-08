# 자연수 하나를 입력 받음
# 입력받은 자연수 개수 만큼 숫자를 공백을 기준 으로 입력 받음
# 자연수 하나를 또 다시 입력받아 위에서 받은 숫자 에서 입력받은 자연수가 포함된 개수를 출력
num = int(input())
nums = list(map(int, input().split()))
cnt = int(input())

print(nums.count(cnt))
