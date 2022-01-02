# 함수의 매개변수

# 매개변수( Parameter ) : 함수로 전달되는 값을 받는 변수 ex. 밑에 width, height
# def getArea(width, height):         #  def 변수(매개변수)
#     return width * height

# 인수 ( Argument ) : 함수 호출 시 함수에게 전달되는 값
# getArea(10,5)      # 10, 5 가 인수


def getAvg(k, e, m):
    return (k+e+m)/3

kor = int(input('국어점수 입력 : '))
eng = int(input('영어점수 입력 : '))
math = int(input('수학점수 입력 : '))

print('평균 : ', getAvg(kor, eng, math))