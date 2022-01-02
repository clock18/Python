# 리스트의 정렬
# 리스트.sort() : 오름차순으로 정렬. 원본을 바꿈
# 리스트.reverse() : 리스트 순서를 역순으로 변경
# sorted(리스트) : 정렬된 결과를 반환, 원본 리스트 변경하지 않음




scores = [90, 78, 81, 64, 99]
print('정렬 전 : ', scores)
scores.sort()
print('정렬 후 : ', scores)

scores = [90, 78, 81, 64, 99]
scores.sort(reverse=True)
print('내림차순 정렬 후 : ', scores)

scores = [90, 78, 81, 64, 99]
scores.reverse()
print('reverse() 적용 후', scores)

scores = [90, 78, 81, 64, 99]
result = sorted(scores)
print(result)
print(scores)



# .sort(key=)

chr = ['b', 'A', 'e', 'C']
print(chr)
chr.sort()
print(chr)
chr.sort(reverse=True)
print(chr)


# 대소문자 구분 없이 정렬
chr = ['b', 'A', 'e', 'C']
print(chr)
chr.sort(key=str.lower, reverse=True)   # key=str.lower 를 주면 abcd 순
print(chr)

# sorted(scores, reverse = True)