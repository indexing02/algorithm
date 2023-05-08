n, m = map(int, input().split())

n_list = [0 for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(a, b + 1):
        n_list[j - 1] = c

for i in n_list:
    print(i, end=' ')
