# import Calculator

from Calculator import add, sub     # from 으로 함수를 불러올 경우에는 함수명을 적을
# print(Calculator.add(10,3))       # 필요가 없음
print(add(10,3))

import Calculator as cal
print(cal.add(10,20))