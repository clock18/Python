# * : 변수 앞에 붙은 경우  ex. *args, **kwargs => 언패킹(unpacking)

def asterisk_test1(a, *args):
    print(a, args)
    print(type(args))

def asterisk_test2(*args):
    print(*args)
    print(type(args))

asterisk_test1(1,2,3,4,5)
asterisk_test2(1,2,3,4,5)

a,b,c = [(1,2,3),(4,5,6),(7,8,9)]
print(a,b,c)
data = [(1,2,3),(4,5,6),(7,8,9)]
print(*data)

def asterisk_test2(a, **args):
    print(a, args)
    print(type(args))