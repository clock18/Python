# 문자열 정렬 : 정렬문자 <, >, ^
# 문자 : 왼쪽 정렬
# 숫자 : 오른쪽 정렬
# < : 왼쪽 정렬
# > : 오른쪽 정렬

string = 'python'
print('{:<10}'.format(string))
print('{:>10}'.format(string))
print('{:^10}'.format(string))
print('{:-^10}'.format(string))


# 문자열.ljust() : 왼쪽정렬
# 문자열.rjust() : 오른쪽정렬
# 문자열.center() : 가운데정렬

print(string.ljust(10))
print(string.rjust(10))
print(string.center(10))
