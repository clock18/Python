# 중첩 for

for y in range(3):
    for x in range(5):
        print(x, end=" ")

    print()

print('-----------------------------------------')


n=0
for y in range(3):
    for x in range(1,5):
        print(x+n, end=" ")
    n+=4
    print()
