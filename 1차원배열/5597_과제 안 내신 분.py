
n = []

for i in range(28):
    n.append(int(input()))

for i in range(30):
    if i+1 not in n:
        print(i+1)