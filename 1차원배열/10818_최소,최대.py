# 정수를 입력받음
# 입력받은 정수 개수만큼 공백을 두고 정수를 입력받음
# 입력받은 정수들 중 최솟값과 최댓값을 공백을 두고 출력

num = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums))
