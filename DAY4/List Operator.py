# 리스트 연산
# 리스트 합치기 : +
# 리스트 곱하기 : *   (반복)
# 리스트 내용 변경

fruits = ['apple', 'banana', 'melon']
a = [1, 'apple', 3.5, [10, 20, 30], True]

# 리스트 합치기
b = fruits + a
print(b)

# 리스트 곱하기
c = fruits * 3
print(c)

# 리스트 내용 변경
a[3] = 'melon'
print(a)

# 리스트 슬라이싱 & 리스트 내용 변경
a[1:3]=[10,11,12]
print(a)

a[0] = [-1,-4]
print(a)