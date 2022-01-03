# 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서 두 숫자를 더한 연산 결과를 저장

f = open('list_num.txt','r')
readList = f.read()
readList_split = readList.split()
readList_len = len(readList_split)




for i in range(0,readList_len,2):
    sum1 = int(readList_split[i]) + int(readList_split[i + 1])
    print('%d + %d = %d' % (int(readList_split[i]), int(readList_split[i + 1]), int(sum1)))

f.close()
