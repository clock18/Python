# Mutable / Immutable

# Mutable : 변경 가능하다는 의미
# Immutable : 변경이 불가능하다는 의미



# 튜플은 변경 불가능 ( Immutable )
x = (1, 2)
y = x
y = y + (3, )
print(x)
print(y)


# 리스트는 변경 가능 ( Mutable )
x = [1, 2]
y = x
y.append(3)
print(x)
print(y)


# 딕셔너리는 변경 가능 ( Mutable )
x = {1:2}
y = x
y[2]=3
print(x)
print(y)

