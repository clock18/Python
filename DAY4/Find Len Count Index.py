# 문자열에서 사용되는 연산 함수들(메소드)
# len, count, find, index, split, replace, join
# upper, lower, capitalize, strip, lstrip, rstrip
# isalpha, isdigit, isspace

# len() = 총 몇개의 글자로 이루어져 있는 지 출력
string = 'programming'
print(len(string))  # 11글자

# 문자열.count('찾을문자') : 문자열 내에 들어있는 특정 문자(열)의 개수 반환
print(string.count('r'))
print(string.count('ing'))

# 문자열.find('찾을문자', start , end)     # start와 end 부분은 안써도 됨(필요할때씀)
crawling = 'Data crawling is fun'
print(crawling.find('is'))          # 찾는 값을 찾았으면 그 글자가 시작되는 주소 반환
print(crawling.find('parsing'))     # 찾는 값이 없으면 -1 반환
print(crawling.find('is',15))       # 15번째 위치부터 is를 찾아라
print(crawling.find('is',5,10))      # 5~10번째 위치사이에서 is를 찾아라

# 문자열.index('찾을문자', start, end)
# 문자열 내에서 특정 문자열의 시작 위치를 반환
# 만약 찾는 값이 없으면, 에러를 반환
print(crawling.index('is'))
print(crawling.index('parsing'))
