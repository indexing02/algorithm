n = int(input())
n_list = list(map(int, input().split()))

m = max(n_list)
ave = 0

for i in range(n):
    n_list[i] = n_list[i] / m * 100
    ave += n_list[i]

print(ave/n)

