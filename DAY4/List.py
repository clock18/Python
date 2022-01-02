# 대괄호 사용
# 리스트 = [값1, 값2 ...]
# ex. scores = [32, 56, 64, 72, 12]
# scores[0] = 32
# scores[1] = 56
# 리스트의 크기는 가변적 : 삽입 ,삭제, 변경 가능

# 다양한 종류의 데이터를 하나의 리스트 안에 저장 가능 : 숫자, 문자열, 논리 혼재 가능
# ex. mylist = [12, "dog", 180.14]

# 리스트는 [] 대괄호 이용

list1 = []
print(list1)
print(type(list1))

list2 = list()
print(list2)
print(type(list2))

list3 = [1,2,3]
print(list3)

list4 = [1,'apple', 3.5,[10,20,30], True]
print(list4)

for l in list4:
    print(l, end=' : ')
    print(type(l))

print('------------------------------------------------')

print('문자열의 길이 : ', len(list4))
for i in range(0, len(list4)):
    print(list4[i], end=' : ')
    print(type(list4[i]))