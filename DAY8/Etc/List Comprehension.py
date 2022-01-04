# List Comprehension
# 리스트를 빠르게, 간결하게 처리 : 파이썬 코드 스타일

# Ex. 정수 0~9까지의 값을 갖는 리스트를 생성하시오.

result = []
for i in range(10):
    result.append(i)
print(result)


## List Comprehension 을 쓴다면 ?
result2 = [i for i in range(10)]
print(result2)



# Ex2. 짝수만 리스트로 생성

result = []
for i in range(10):
    if i%2 == 0:
        result.append(i)


## List Comprehension
result2 = [i for i in range(10) if i%2==0]
print(result2)

result2 = [i if i%2==0 else 11 for i in range(10) ]     # 11 자리에는 짝수가 아닐 때
print(result2)                                          # 출력될 문자를 입력하면 됨



# Ex3. 중첩 반복문

list1 = ['a', 'b', 'c']
list2 = ['D', 'E', 'F']

result = []
for i in list1:
    for j in list2:
        result.append(i+j)
print(result)


result = [i+j for i in list1 for j in list2]
print(result)



# Ex4.
words = 'Remember to let her into your heart'.split()
print(words)

# result = [[(w.upper(), w.lower(), len(w)] for w in words]
# print(result)