# 리스트를 함수에 전달할 경우

def show_list(myList):
    print(myList)

def modify_list(myList):
    myList.append('new')
    print(myList)


myList = [1, 2, 3, 4]       # 리스트는 가지고 있는 원본을 공유하는 형태가 됨
show_list(myList)           # 따라서 참조하여 수정할 때는 주의해야 함
print(myList)
modify_list(myList)
print(myList)



# 딕셔너리를 함수에 전달할 경우
students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}]

def get_student_info(stdList):
    name = stdList['name']
    return {'name' : name}

for std in students:
    stdInfo = get_student_info(std)