# 텍스트 파일 읽기 : read()
# 내용 전체를 읽어서 1개의 문자열로 반환

f = open('test2.txt','r')
data = f.read()
print(data)
f.close()

# for ch in data:
#     print(ch)

