# 문제. 각 학생별 점수 리스트 생성

# 학생별 총점과 평균 점수 출력
# 과목별 총점과 평균 점수 출력


kim = [90, 85, 70]
choi = [88, 92, 72]
kang = [100, 95, 100]
lee = [90, 60, 70]

students = [kim, choi, kang, lee]

for i in range(4):
    sum = 0
    avg = 0
    for j in range(3):
        sum += students[i][j]
    avg = sum / 3
    print('%s의 총점은 %d이고, 평균은 %.2f입니다.'%(students[i],sum,avg))


print('----------------------------------------------------------------')




kim = [90, 85, 70]
choi = [88, 92, 72]
kang = [100, 95, 100]
lee = [90, 60, 70]

students = [kim, choi, kang, lee]

for i in range(3):
    sum = 0
    avg = 0
    for j in range(4):
        sum += students[j][i]
    avg = sum / 4
    print('%d번째 과목의 합은 %d이고, 평균은 %.2f입니다' %(i+1, sum, avg))



# round() : 반올림하는 함수

