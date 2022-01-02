# 문자열 변경 : a.replace(찾는 문자열, 변경할 문자열)
# 전체 문자열에서 특정 문자열을 찾아서 다른 문자열로 변경
# 찾는 문자열이 존재하면 변경할 문자열로 대체하여 반환
# 찾는 문자열이 없다면 바꿀 것이 없기 때문에 원래 문자열을 반환

lan = 'Python programming'

print(lan)
print(lan.replace('Python','Java'))
print(lan.replace('on','om'))
print(lan.replace('oq','Java'))     # 찾을 문자가 없는 경우 그대로 반환됨