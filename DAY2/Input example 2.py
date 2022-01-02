# 연습문제

# 국어점수 입력 : 90
# 영어점수 입력 : 90
# 수학점수 입력 : 70
# 총점 : 250
# 평균 : 83.33

kor = input('국어점수 입력 : ')
eng = input('영어점수 입력 : ')
math = input('수학점수 입력 : ')
sum = kor+eng+math
print('총점 : %d'%sum)
avg = sum/3
print('평균 : %.2f'%avg)



# 연습문제 2
# BMI 지수 계산식 : 몸무게 / (키*키)

# 입력형식
# 몸무게(kg) :
# 키(미터) :

# 출력
# 당신의 BMI는    입니다.


weight = int((input('몸무게(kg) : ')))
height = int((input('키(미터) : ')))
BMI = weight / (height*height)
print('당신의 BMI는 %f입니다.'%BMI)
print('당신의 BMI는 {} 입니다.'.format(BMI))

