# 리스트 인덱싱 ( indexing )
# 리스트에서 인덱스 연산자를 통하여 요소를 참조/접근하는 것

a = [1, 'apple', 3.5, [10, 20, 30], True]

print(a[0])         # 첫 번째 요소 출력
print(a[-1])        # 맨 마지막 요소 출력
print(a[-5])
print(a[3][-1])     # [10, 20, 20] 중에서 맨 마지막 요소 출력

b = ['apple', 'banana', 'melon']

c= [a,b]
print(c)

print(c[0][3][-1])