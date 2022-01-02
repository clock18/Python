# 학생 n명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하여 출력하기

scores = []
sum = 0
avg = 0
n = int(input('학생 수 입력 : '))
for i in range(1,n+1):
    score = int(input('학생 %d 점수 입력 : '%i))
    if 0 <= score <= 100 :
        scores.append(score)
    else:
        continue
    sum += score
    avg = sum / len(scores)

print(sum)
print(avg)