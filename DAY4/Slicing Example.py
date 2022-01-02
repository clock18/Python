# 문자열 슬라이싱 ( slicing )

crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'

print(crawling)
print(crawling[0])
print(crawling[-1])
print(crawling[0:4])    # 0~3 번째 까지의 문자들을 가져옴 = Data
print(crawling[17:])    # 17번째부터 끝까지 = fun
print(crawling[:18])
print(crawling[-1:])    # 마지막 글자 = n
print(crawling[:-1])
print(crawling[10:10+4])

print(parsing[:])   # 전체 다 가져옴
