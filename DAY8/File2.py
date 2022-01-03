# 파일에 쓰기

# data = 'Hi'
# f = open('file2.txt','w')
# f.write(data)
# f.close()

# data = '안녕하세요'
# f = open('file2.txt','w')         # 파이참에서 열면 한글이 깨져서 나옴
# f.write(data)
# f.close()

data = '안녕하세요'
f = open('file3.txt','w', encoding='utf-8')       # 파이참에서 열어도 한글이 그대로 나옴
f.write(data)
f.close()