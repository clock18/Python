# 입력 내용이 긴 경우, 여러 줄에 작성해야 하는 경우

sum1 = 1+2+3+4+\
5+6+7

sum2 = (1+2+3+4+
       5+6+7)

# escape character
# ex. \n: 줄바꿈
# \t : tap ( 한 번 누르면 4칸띄워짐 )
# \' : '
# \" : "
# \\ : \

# print('don\'t')
# print('123\t456')
# print('he said, "yes"')
# print("he said, \"yes\"")
# print('c:\pythonStudy\day2')
# print(r'c:\pythonStudy\name')
# escape 문자가 아님을 나타내기 위해서 맨 앞에 r을 붙인다 ( remove )
# 바로 위의 예시같은 경우 \n이 escape character가 아님을 나타내기 위해 r을 붙임

# 2개 명령어 ( 문장 ) 을 한 줄에 입력 : 중간에 ; 을 넣으면 됨.
print(sum1) ; print(sum2)
print('apple \nbanana \nmelon')
print('apple', end=' ')
print('banana', end=' ')
print('melon')
print('apple banana melon')
