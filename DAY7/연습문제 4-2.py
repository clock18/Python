# 2. 문자열 분리, 추출해서 합계 구하기

str_data = "{a1:20},{a2:30},{a3:15}, \
 {a4:50},{a5:-14},{a6:15},\
 {a7:20},{a8:70},{a9:-100}"

split_data = str_data.split(',')
total = 0
n = 0
for data in split_data:
    item = data.split(':')
    item2 = item[1].split('}')
    score = int(item2[0])
    print(score)
    total += score
    n += 1

print('총점 : %d, 평균 : %f'%(total, total/n))