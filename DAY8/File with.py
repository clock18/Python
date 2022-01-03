# with 문
# with 문이 종료되면 파일객체는 자동으로 close()
# with open(파일명, 열기모드) as 파일객체:
#       수행코드

# with open('test3.txt','w') as f:
#     f.write('hello')

file = 'test3.txt'
data = 'Python Programming'

with open(file,'w') as f:
    f.write(data)