# 정적 메서드 ( static method )
# 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
# 메서드 위에 @staticmethod를 쓰면 됨
# 그리고 메서드에 self를 넣지 않음

class Calc:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def mul(a,b):
        return a*b

calc1 = Calc()
calc2 = Calc()
print(calc1.add(3,2))
print(calc1.mul(3,2))