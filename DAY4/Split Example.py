# 생년월일을 입력하고 연도, 월, 일을 구분해서 출력

# 생일 입력(연/월/일) : 2000/02/01
# 당신은 2000년에 태어났고
# 생일은 02월 07일 이군요


birth = input('생일 입력(연/월/일) : ')
bitrh_list = birth.split('/')
print(f'당신은 {bitrh_list[0]}년에 태어났고\n생일은 {bitrh_list[1]}월 {bitrh_list[2]}일 이군요')


