num1, num2 = map(int, input().split())

n_list1, n_list2 = [], []

for i in range(num1):
    nums1 = list(map(int, input().split()))
    n_list1.append(nums1)

for i in range(num1):
    nums2 = list(map(int, input().split()))
    n_list2.append(nums2)

for i in range(num1):
    for j in range(num2):
        print(n_list1[i][j] + n_list2[i][j], end=" ")
    print()
