# readline() : 한 줄씩 읽어오기

# 한 줄만 읽어오기
f = open('test.txt','r')
line = f.readline()         # 첫 번째 라인 1개 읽어오기
print(line)
f.close()                   # 다른이름으로저장 => ansi 파일로 저장


# 한 줄씩 읽어오기
f2 = open('test.txt','r')

while True:
    line = f2.readline()        # 한 줄을 읽어오고 \n 한 후, 다음 한 줄을 가져옴
    if not line:
        break
    print(line, end='')         # \n 처리 안한것을 보고 싶다면 end='' 입력

f2.close()