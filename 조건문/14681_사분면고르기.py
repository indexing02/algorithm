# (12,5)-> 1사분면
# (-12,5) -> 2사분면
# (-12, -5) -> 3사분면
# (12,-5) -> 4사분면

a = int(input())
b = int(input())

if a > 0 and b > 0:
    print(1)
elif a < 0 < b:
    print(2)
elif a < 0 and b < 0:
    print(3)
else:
    print(4)
