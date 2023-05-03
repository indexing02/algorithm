# 첫째줄에는 영수증에 적인 총 금액이 주어짐
# 둘째줄에는 영수증에 적힌 구매한 물건의 종류의 수가 주어짐
# 이후 각 물건의 가격과 개수가 공백을 두고 주어짐
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치 하면 Yes 아니면 No 출력

total_price = int(input())
total_amount = int(input())

price_sum = 0

for i in range(total_amount):
    price, amount = map(int, input().split())
    price_sum += price*amount

if price_sum == total_price:
    print('Yes')
else:
    print('No')

