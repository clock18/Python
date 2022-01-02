# 문자열 분리
# 문자열.split() : 구분자(공백, 세미콜론, 콜론, 콤마 ...)를 기준으로 문자열 나눔
# 리스트로 반환

cities = '인천 대구 대전 부산 울산 청주 춘천'
cities_split = cities.split()   # 괄호안에 아무것도 안쓰면 공백을 기준으로 짜름
print(cities_split)     # 공백을 기준으로 짜름


names = '성춘향;변학도;이몽룡;방자'
names_split = names.split(';')      # 세미콜론을 기준으로 나누어라
print(names_split)