# 제어문 = 조건문 + 반복문

# 조건문 = if 문
# 반복문 = for문, while문
# 기타 제어문 = continue문 break문

# if문 : 조건식이 참이면 주어진 문장 수행
#       조건식이 거짓이면 아무것도 수행하지 않음
#       if (조건식) : 참일 경우 수행되는 문장 (if다음에 들여쓰기 필수)

# if ~ else 문
# 조건식이 참이면 if문 수행, 거짓이면 else문 수행


# 문제 : id와 password를 입력받아 둘 다 맞으면 로그인 성공 출력,
#       하나라도 틀리면 로그인 실패 출력

id = input('ID입력 : ')
password = int(input('password입력 : '))
if id=='multicampus' and password==1234 :
    print('로그인 성공')
else :
    print('로그인 실패')

단체 주석 처리 : ctrl + /

# 중첩 if
if id=='multicampus':
    if pw==1234:
        print("로그인 성공")
    else:
        print("비밀번호가 다릅니다.")
else:
    print("아이디가 다릅니다.")


# 문제 : 정수를 입력받아서 홀수인지 짝수인지 판별하여 출력
# 정수 입력 :
# 홀수 입력 :

정수 = int(input( '정수 입력 :' ))
if 정수%2==0:
    print('짝수')
else :
    print('홀수')


# 입력한 정수가 음수, 0, 양수 인지를 확인하여 출력

if num > 0:
    print('양수')
else:
    if num == 0:
        print('0')
    else:
        print('음수')

if num > 0:
    print('양수')
elif num == 0:
    print('0')
else:
    print('음수')


# 문제 : 점수를 입력받아서 학점 출력 A, B, C, D, F

grade = float(input( '학점 출력 : '))
if grade>=90:
    print('A')
elif grade>=80:
    print('B')
elif grade>=70:
    print('C')
elif grade>=60:
    print('D')
else :
   print('F')
