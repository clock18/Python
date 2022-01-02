# 반환값이 여러 개인 경우

def multi_return():
    return 1, 2, 3          # ,를쓰면 tuple을 정의하는 것이므로 튜플로 출력됨.
                            # 하지만 []를 쓰면 list형태로 출력하는 것도 가능함.

result = multi_return()     # 굳이 안해도 됨.
print(result)               # multi_return()을 바로 입력해도 출력됨.


a, b, c = multi_return()
print(a,b,c)

# return 문이 여러개 사용될 경우 : 가장 첫번째 return 문장만 실행됨.