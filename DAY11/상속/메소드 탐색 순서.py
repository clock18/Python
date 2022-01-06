# 메소드 탐색 순서 ( Method Resolution Order : MRO )
# 동일한 이름의 메소드를 갖는 경우

class A:
    def greeting(self):
        print('a')

class B:
    def greeting(self):
        print('b')

class C:
    def greeting(self):
        print('c')

class D(B,C):
    pass

x = D()
x.greeting()
print(D.mro())          # 출력 순서를 보여줌

