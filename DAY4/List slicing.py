# 리스트 슬라이싱 ( slicing )
# [start:end] : start에서 end-1 요소까지 선택
# 슬라이싱 연산 결과는 리스트 반환

# a[:n] : 처음부터 n-1 요소까지
# a[start:] : start 부터 마지막 요소까지
# a[:] : 처음부터 끝까지
# a[:-1] : 처음부터 마지막-1 까지
# a[-1:] : 마지막 요소하나 출력
# a[n:] : n부터 끝까지


a = [1, 'apple', 3.5, [10, 20, 30], True]
print(a[:])
print(a[3:])
print(a[:3])
print(a[2:4])
print(a[-1:])
print(a[:-1])