
num_list = []

for i in range(9):
    nums = list(map(int, input().split()))
    num_list.append(nums)

max_n = -1
max1 = 0
max2 = 0

for i in range(9):
    for j in range(9):
        if max_n < num_list[i][j]:
            max_n = num_list[i][j]
            max1 = i+1
            max2 = j+1

print(max_n)
print(max1, max2)

