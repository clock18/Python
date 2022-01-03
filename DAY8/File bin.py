# 이진 파일 : 글자가 아닌 비트 단위로 의미가 있는 파일
# ex. 그림파일, 음악파일, 동영상파일, 엑셀파일, 한글파일, 실행(exe)파일

# write()
# read(1) : 1바이트씩 읽기

# 이진파일 읽기
bin = open('c:/windows/notepad.exe','rb')   # rb = read bin


# 이진파일 쓰기
bout = open('c:/Temp/notepad.exe','wb')     # wb = write bin

while True:
    inStr = bin.read(1)
    if not inStr:
        break
    bout.write(inStr)
bin.close()
bout.close()
