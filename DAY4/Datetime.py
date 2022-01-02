from datetime import date, datetime  # datetime을 쓰기위해 선언 필수

print(date.today())     # 연.월.일
print(datetime.today())     # 연,월,일,시,분,초 까지 나옴

today = date.today()
year = today.year
month = today.month
day = today.day

print(f'연도 : {year}, 월 : {month}, 일 : {day}')

print(datetime.now())

current_time = datetime.now().time()
time = datetime.now().time().hour
minute = datetime.now().time().minute
second = datetime.now().time().second
microsec = datetime.now().time().microsecond

print(time, minute, second, microsec)


# 날짜계산 : timedelta() 함수 사용

from datetime import date, datetime, timedelta

print(today + timedelta(days=-1))
print(today + timedelta(days=1))
print(today + timedelta(days=-7))
print(today + timedelta(days=7))

cur_now = datetime.now()
print(cur_now + timedelta(hours=-1))


# strftime()함수 : 날짜 형식을 문자열로 반환
# H : 24시간
print(today.strftime('%Y-%m %d %H:%M:%S'))

print(type(today))

# strptime()함수 : 문자열을 날짜형식으로 반환
today = '2020-06-20 17:40:20'
tod = datetime.strptime(today, '%Y-%m %d %H:%M:%S')
print(tod)