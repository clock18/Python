# 학생 10명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하여 출력하기
# 학생1 점수 입력 : 90
# 총점 : 416
# 평균 : 83.20

score = []
sum = 0
for student in range(1,11):
    scores = int(input('학생%d 점수 입력 : '%student))
    sum += scores
    score.append(scores)

avg = sum//10
print(score)
print('총점 : %d'%sum)
print('평균 : %.2f'%avg)

