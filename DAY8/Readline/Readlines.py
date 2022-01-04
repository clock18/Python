# readlines() : 전체 라인을 읽어오기
# 한 행이 리스트의 요소가 됨

# f = open('test.txt','r')
# lines = f.readlines()
# print(lines)
# f.close()


f = open('../list_num.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line.split())
f.close()


# f = open('test.txt','r', encoding='utf-8')
# lines = f.readlines()
# for line in f:
#     print(lines,end='')
# f.close()