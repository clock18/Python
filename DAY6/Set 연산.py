# Set의 연산

A = {1, 2, 3}
B = {3, 4, 5}

# 1) 교집함
C = A & B
print(C)

C = A.intersection(B)
print(C)


# 2) 합집함
C = A | B
print(C)

C = A.union(B)
print(C)


# 3) 차집함
C = A - B
print(C)

C = A.difference(B)
print(C)


D = B- A
print(D)