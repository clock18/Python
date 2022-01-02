# 상품 가격, 주문 수량을 입력받아서 주문액을 계산하여 반환하는 함수 작성

# 상품 가격 입력 :

# def order():
#     a = int(input('상품가격 입력 : '))
#     b = int(input('수문수량 입력 : '))
#     print('-------------------------------')
#     c = a * b
#     print('상품가격 : %d'%a)
#     print('주문수량 : %d'%b)
#     print('주문액 : %d'%c)
#
# order()



def order():
    a = int(input('상품가격 입력 : '))
    b = int(input('수문수량 입력 : '))
    c = a * b
    return a, b, c      # 반환값

a, b, c = order()
print('-------------------------------')
print('상품가격 : %d'%a)
print('주문수량 : %d'%b)
print('주문액 : %d'%c)

# result = order()
# result[0], result[1]
