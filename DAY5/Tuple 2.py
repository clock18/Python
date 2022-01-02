# 튜플 사용

# 튜플 요소 접근 : indexing

t1 = (10, 30, -10, 50, 100)
print(t1[0] + t1[3])


# 튜플 범위에 접근 : slicing

print(t1[1:3])


# 2차원 튜플
tt = ((1,2,3),(4,5,6),(7,8,9))
print(tt)
print(tt[0][-1])


# 튜플 원소 추가하는 방법
mytuple = (10,20,30)
my_list = list(mytuple)
my_list.append(40)
mytuple = tuple(my_list)
print(mytuple)

