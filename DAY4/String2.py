# 문자열 구성 파악
# 문자열.isalpha() : 문자 여부 결과 반환( 맞으면 True, 틀리면 False )
# 문자열.isdigit() : 숫자인 지 여부 결과 반환
# 문자열.isspace() : 하나의 문자에 대하여 공백여부 반환
# 문자열.isalnum() : 문자 또는 숫자인지 확인
# 문자열.islower() : 소문자 여부
# 문자열.isupper() : 대문자 여부


string = '내 이름은 jhjung이고 나이는 27입니다'
str_split = string.split()
for result in str_split:
    if result.isdigit():
        print('숫자군요')
    else:
        print('숫자가 아니군요')


print('---------------------------------------------')


# 입력된 문자열에서 알파벳의 개수, 숫자의 개수, 스페이스의 개수, 기타의 개수를 각각 계산하여 출력
# 문장을 입력하세요 : 내 이름은 jhjung이고 내 메일은 clock18@naver.com 입니다.

put = input('문장을 입력하세요 : ')
alpha = 0
num = 0
space = 0
etc = 0

for x in put:
    if x.isalpha():
        alpha += 1
    elif x.isdigit():
        num += 1
    elif x.isspace():
        space += 1
    else:
        etc += 1

print('알파벳의 개수는 : %d 입니다'%alpha)        # 알파벳, 한글 모두 알파벳으로 취급함
print('숫자의 개수는 : %d 입니다'%num)
print('공백의 개수는 : %d 입니다'%space)
print('기타의 개수는 : %d 입니다'%etc)

