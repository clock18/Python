# 리스트의 요소 제거

# remove(값) : 왼쪽부터 시작해서 제일 첫 번째 만나는 값을 하나 지움.
#              여러개를 지우고 싶으면 반복문 사용해야 함.

# pop() : 마지막 값을 반환하고 마지막 요소를 제거
# pop(index) : index 위치 요소 값을 제거

x = ['apple', 'banana', 'coconut', 'melon', 'banana', 'apple']

x.remove('melon')
print(x)

n = x.count('banana')
for i in range(n):
    x.remove('banana')
print(x)

y = [1,3,5,1,10]
last = y.pop()
print(y)
print(last)

y.append(-10)
print(y)
rm = y.pop(3)   # pop() : 괄호 안에 숫자를 넣으면 그 숫자 자리에 있는 값을 제거해줌
print(y)

