num = int(input())

m = [1, 0, 0]

for i in range(num):
    num1, num2 = map(int, input().split())
    m[num1 - 1], m[num2 - 1] = m[num2 - 1], m[num1 - 1]

for i in range(len(m)):
    if m[i] == 1:
        print(i + 1)
