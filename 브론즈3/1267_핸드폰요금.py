num = int(input())
nums = list(map(int, input().split()))

p1 = 0
p2 = 0

for i in range(len(nums)):
    p1 += (nums[i] // 30 + 1) * 10

for i in range(len(nums)):
    p2 += (nums[i] // 60 + 1) * 15

if p1 < p2:
    print("Y", p1)
elif p1 == p2:
    print("Y", "M", p1)
else:
    print("M", p2)


