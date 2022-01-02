# 도시명을 입력하고 해당 도시가 있는지 유무를 출력하기

# in을 이용한 경우

# cities = '인천 대구 대전 부산 울산 청주 춘천'
#
# city = input('도시명 입력 : ')
#
# if city in cities:
#     print('해당 도시가 있습니다.')
# else:
#     print('해당 도시가 없습니다.')



# find를 이용할 경우

cities = '인천 대구 대전 부산 울산 청주 춘천'

city = input('도시명 입력 : ')

if cities.find(city) != -1:
    print('해당 도시가 있습니다.')
else:
    print('해당 도시가 없습니다.')
