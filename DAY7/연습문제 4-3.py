num = str(input('숫자를 여러개 입력하세요. '))
len1 = len(num)

for heart in range(0,len1):
    print('\u2665'*int(num[heart]))