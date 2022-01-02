# format() 함수 사용
# .format 은 앞에 string형식이 왔을 때 사용가능

s = '{0:d} {1:5d} {2:05d}'.format(123, 123, 123)
s2 = '%d %5d %05d' % (123, 123, 123)

# 05d = 5자리 정수를 만드는데 뒷부분이 남으면 0으로 채움
# ex 369 같은 경우 00369가 됨.

# {0:d} 같은 경우 .format(0번째자리, 1번째자리, 2번째자리) 에서 0번쨰 자리의
# 숫자가 할당됨을 의미.

# 5d = 5자리 정수를 만드는데 뒷부분이 남으면 공백으로 채움
# ex. 369 같은 경우   369가 됨.

print(s)
print(s2)

# f'String
# ex. print(f'{1234})

tea = 'coffee'
n = 5
s3 = f'{tea} {n}'
print(s3)

for month in ['1월','2월','3월']:
    print(f'{month}')

