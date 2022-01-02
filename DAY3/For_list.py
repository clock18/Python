# for에서 리스트를 이용
# 학생 성적 리스트 score = [70, 90, 100, 50 ,85]

# 60점이상 합격, 60점미만은 불합격 출력
# 1번 학생 합격
# 2번 학생 합격
# 5번 학생 합격
# score = [70, 90, 100, 50 ,85]
# n=0
# for i in score:
#     n+=1
#     if i >= 60:
#         print('%d번 학생은 합격입니다.'%n)
#     else:
#         print('%d번 학생은 불합격입니다.'%n)



pos = 0
neg = 0
zero=0

for i in range(1,11):
    num1 = int(input('숫자%d입력 : '%i))
    if num1 > 0:
        pos += 1
    elif num1 < 0:
        neg += 1
    else:
        zero += 1

print("양의 개수 : %d"%pos)
print('음의 개수 : %d' % neg)
print('0의 개수 : %d'%zero)