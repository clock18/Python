# 문제
# 주문액이 10만원 이상이면 10% 할인
# 주문액이 5만원이상 10만원 미만이면 5% 할인
# 주문액이 5만원미만이면 할인없음

def order(price, qt):
   amount = price * qt
   if amount >= 100000:
       discount = amount * 0.1
   elif amount >= 50000 :
       discount = amount * 0.05
   else:
       discount = 0
   result = amount - discount
   return amount, discount, result      # 반환값이 여러개인 경우 튜플 형태로 반환

price = int(input('상품가격 입력 : '))
qt = int(input('주문수량 입력 : '))
amount, discount, result = order(price, qt)     # 변수 호출

print(f'주문액:{amount}')
print(f'할인액:{discount}')
print(f'지불액:{result}')