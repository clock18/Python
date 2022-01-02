# 참고 사이트 : https://docs.python.org/ko/3/library/functions.html

# abs() : 절대값
# all() : 모든 요소가 참이면 True ( False = 0 , True = 0이 아닌 값 )
# iterable ( 반복 가능한 자료형 ) : 리스트, 튜플, 딕셔너리, 집합 ( for 반복문 이용 )
# any() : 하나라도 참이면 True   ex. ''같은 빈 문자열이나 []같은 빈 리스트도 False 처리

# bool() : bool값으로 변환 ( True or False )
# chr() : 아스키코드 값에 해당하는 문자 반환
# print(chr(65))

# ord() : 문자에 대한 아스키코드 값 반환

# divmod(a,b) : a를 b로 나눈 몫과 나머지 반환
# print(divmod(10,3))     # 반환 값은 튜플 형태. (몫, 나머지)형태로 출력
#
# enumerate() : 시퀀스를 인덱스값을 포함해서 enumerate형의 객체로 반환
# 시퀀스 : range(), 문자열, 리스트, 튜플
# print(enumerate('hello'))
# for i, c in enumerate('hello'):
#     print(i, c)
#
# for i, season in enumerate(['봄','여름','가을','겨울']):
#     print(i, season)

# eval(표현식) : 표현식의 연산 결과 반환
# a=1
# b=2
# print(eval('a+b'))
# print(type(eval('10')))

# filter(function, iterable) : function으로 iterable을 걸러냄

def positive(x):
    return x>0

print(filter(positive, [0,1,-1,10,-3,5]))
print(list(filter(positive, [0,1,-1,10,-3,5])))


def even(x):
    if x%2==0:
        return x
print(list(filter(even,[0,1,-1,10,-3,5])))


# help() : 도움말

# pow(x,y) : x의 y승
# print(pow(10,3))
#
#
#
# range()
# print(range(0,5))
# print(list(range(0,5)))


# zip(*iterable) : iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환

print(zip([1,2,3],[4,5,6]))
print(list(zip([1,2,3],[4,5,6])))

keys = ['apple','melon','banana']
vals = [250,300,400]

print(list(zip(keys,vals)))
print(dict(zip(keys,vals)))