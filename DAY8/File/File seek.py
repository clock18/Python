# 파일 내에서 검색
# seek(offset, whence)
# offset : 시작 위치로부터 열의 위치
# whence : 위치 ( 0 = 시작위치, 1 = 현재위치, 2 = 파일의 끝 )

# seek(0,0) : 시작위치로부터 0열에 위치 => 0행 0열
# seek(10,0) : 시작위치로부터 오른쪽으로 10열 이동한 위치 => 0행 10열
# seek(0,2) : 파일 끝에서부터 0열의 위치

f = open('../test2.txt', 'r')
# f.seek(0,0)           # 메모장에서 엔터를 치면 \r\n 이 보이지 않게 자동 입력되어 있음
f.seek(0,2)
# /r : carriage return ( 무조건 첫 번째 열로 이동 )
# /n : line feed

lines = f.readlines()
print(lines)
f.close()