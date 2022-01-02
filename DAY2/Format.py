kor=90
eng=80
math=80

score=kor+eng+math
average=score/3
print('총점 : %d,평균 : %.2f'%(score,average))

print(format('총점:%d,평균:%.2f')%(score,average))

# 총점 = total tot score sum
# 평균 = average avg
# 10.2f = 전체 10자리 중 소수점 2자리까지만 표현

print('name:{} phone:{}'.format('정진한','010-1234-5678'))
print('name:{1} phone:{0}'.format('010-1234-5678','정진한'))