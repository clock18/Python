# 딕셔너리 ( dictionary )
# key와 value의 한 쌍을 요소로 갖는 자료형
# 딕셔너리 = {key1:value1, key2:value2, ...}
#           ex. d = {1:'a', 2:'b', 3:'c'}
# 중괄호 사용
# 딕셔너리 생성 : {} or dict()


students = {1:'최선', 2:'홍길동', 3:'강감찬'}

print(students)
print(type(students))
print(students[1])


prof = {}
prof[1] = '이순신'
prof[2] = '홍길동'
print(prof)


member = {'name':'홍길동', 'phone':'010-1234-5678'}
print(member)
print(member['name'])


member1 = {'name':'홍길동', 'phone':'010-1234-5678', 'name':'이순신'}
#   중복되는 키가 있으면 최근의 것으로 변경된다.
print(member1)


naver = {'name' : 'naver', 'url' : 'www.naver.com', 'id' : 'clock18'}
google = {'name' : 'google',
          'url' : 'www.google.com',
          'id' : 'clock18'}    # 중괄호는 이렇게 한 괄호 안에서 엔터키를 눌러도 된다.


# keys(), values(), items()
print(naver.keys())
print(naver.values())
print(naver.items())

for key in naver.keys():
    print(key)

for value in naver.values():
    print(value)

for item in naver.items():
    print(item)



# key로 value 찾기
print(naver['name'])
print(naver.get('name'))
print(naver.get('passwd', '없음'))    # 찾고자 하는 문자가 없을 때 없음을 출력함.

key = 'passwd'
if naver.get(key) is None:
    print(key + '에 대한 값이 없습니다')

if key not in naver:
    print(key + '에 대한 값이 없습니다')