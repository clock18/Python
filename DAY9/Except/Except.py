# 예외 처리
# 에러 종류와 상관없이 에러가 발생하면 처리하기

# 예외 처리 형식
# try:
#     에러가 발생할 문장들
# except:
#     에러가 발생하면 처리할 코드
# else:
#     에러가 발생하지 않으면 처리하는 문장
# finally:
#     에러와 상관없이 항상 수행하는 문장


# 에러의 종류와 상관없이 에러를 처리하는 경우
# 예제1. 0으로 나누는 경우 처리
# try:
#     # print(10/0)
#     print('나이 : ' + 23 + '살')
# except:
#     # print('0으로 나눌 수 없습니다')
#     print('오류 발생')


# 특정 에러를 기입하는 경우
# 에러 종류 명시 처리
try:
    print(10/0)

except ZeroDivisionError as e:      # e = 에러 메시지 변수 ( 내가 정할 수 있음 )
    print('0으로 나눌 수 없습니다',e)


# ValueError
try:
    num = int(input('숫자를 입력하세요 : '))
except ValueError:
    print('숫자가 아닙니다.')
