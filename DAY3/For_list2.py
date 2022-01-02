# 리스트에 있는 이름인지 확인

names = ['베토벤', '홍길동','변학도', '아쿠아맨']

x = input('이름 입력 : ')
for name in names :
    if x == name:
        find = True
        break
    else:
        find = False

if find:
    print('명단에 있어요')
else:
    print('명단에 없어요')