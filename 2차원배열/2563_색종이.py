num = int(input())

width = num*100

num1 = []
num2 = []

for i in range(num):
    n1, n2 = map(int, input().split())
    num1.append(n1)
    num2.append(n2)

for i in range(num - 1):
    for j in range(i + 1, num):
        if -10 < num1[i] - num1[j] < 10:
            if num1[i] < num1[j]:
                n1 = num1[i] + 10 - num1[j]
            elif num1[i] > num1[j]:
                n1 = num1[j] + 10 - num1[i]
            else:
                n1 = 10
                continue
            n2 = abs(num2[i] - num2[j])
            width -= n1*n2

print(width)

