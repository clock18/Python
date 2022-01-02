th = input('도형 입력 : ')
width=10
height=20
radius=10
area=width*height
area2=(width*height)//2
area3=3.1416*(radius*radius)

if th=='사각형':
    print('사각형의 면적 = %.2f'%area)
elif th=='삼각형':
    print('삼각형의 면적 = %.2f'%area2)
else :
    print('원의 면적 = %.2f'%area3)