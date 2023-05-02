# 세 자리 자연수가 주어질 때 곱셉 과정을 출력
a = int(input())
b = input()

a1 = a*int(b[2])
a2 = a*int(b[1])
a3 = a*int(b[0])
a4 = a*int(b)

print(a1, a2, a3, a4, sep='\n')