# 리스트 복사

# 얕은 복사(shallow copy) : 실제 리스트는 복사되지 않고 참조값(주소)만 복사
a = [1,2,3,4]
b = a
print(a)
print(b)

a[-1]=100
print(a)
print(b)

# 깊은 복사(deep copy)
# 리스트 복사본을 새로 생성하여 반환
# list()함수 또는 deepcopy()함수 사용   # copy함수는 import해야하므로 list가 편함
print('-----deep copy-----')
c = list(a)
print(c)
c[0] = 'apple'
print(a)
print(c)

import copy
d = ['a','b','c']
e = copy.deepcopy(d)

e[0] = 1
print(d)
print(e)