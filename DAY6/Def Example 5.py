# 리스트 반환
# 3명 이름을 입력 받아서 리스트에 저장하고 리스트를 반환하는 함수
# get_names()

# def get_names():
#     names = []
#     for i in range(3):
#         name = input('이름 입력 : ')
#         names.append(name)
#     return names
#
# namelist = get_names()
#
# print(namelist)



# 이름과 나이를 입력받고 그 정보를 딕셔너리 형식으로 반환
# get_info()

def get_info():
    name = input('이름 입력 : ')
    age = int(input('나이 입력 : '))
    info = {'name':name, 'age':age}
    return info

std_info = get_info()
print(std_info)
print(get_info())