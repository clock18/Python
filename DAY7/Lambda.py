# Lambda ( 람다 )
# 사용볍 => lambda 매개변수 : 식

# def add(x,y):
#     result = x + y
#      return result
#
# print(add(10,20))
#
# add2 = lambda x,y : x + y
# print(add2(10,2))
#
# add3 = lambda x=10,y=10 : x + y
# print(add3(10,20))
# print(add3())
#
#
# 문제. 리스트의 각 요소에 10을 더하는 함수
#
def add10(numList):
    for i in range(len(numList)):
        numList[i] += 10

num = [10,20,30]
add10(num)
print(num)
#
#
#
# def add10(num):
#     return num + 10
#
# for i in range(len(num)):
#     num[i] = add10(num[i])
#
# print(num)



# map()
#
# num2 = list(map(add10, num))
# print(num2)
#
# # lambda & map()
# num3 = list(map(lambda num : num+10, num))
# print(num3)


# 문제
# map을 이용하는 경우
# number1 = [3.5, 3.5, 2.0, 4.6]
# print(list(map(int,number1)))       # map(식, 식이 적용될 범위)
                                      # 범위안의 요소 갯수만큼 반복
# for을 이용하는 경우
# number1 = [3.5, 3.5, 2.0, 4.6]
# for x in range(len(number1)):
#     number1[x] = int(number1[x])
# print(number1)


# 문제2. 두 리스트의 각 자리수의 값을 합해서 새로운 리스트를 생성

# 2-1)
list1 = [1,2,3,4]
list2 = [10,20,30,40]

def addList(x,y):
    a = []
    for i in range(len(x)):
        a.append(x[i]+y[i])
    return a
print(addList(list1,list2))


# 2-2)
print(list(map(lambda x,y : x+y, list1,list2)))