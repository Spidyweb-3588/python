import pendulum

# 타임존 설정
dt = pendulum.datetime(2022,3,3, tz="Asia/Seoul")
print(type(dt), dt)
print("\n")

#로컬 시간 출력
dt_2 = pendulum.local(2022,3,3)
print(dt_2)
print("\n")

#현재(로컬)시간 출력
now = pendulum.now()
print(now)
print("\n")

#지원언어를 한국어로 설정
pendulum.set_locale('ko')
#현재로 부터 1년을 더한 값을 한국어로 설명
print(pendulum.now().add(years=1).diff_for_humans())
print("\n")

#시간을 입력받아 파싱 후 세부적으로 접근
dt_3 = pendulum.parse('2022-03-03T22:00:00')

print(dt_3.year)
print(dt_3.month)
print(dt_3.day)
print(dt_3.hour)
print(dt_3.minute)
print(dt_3.second)
print(dt_3.microsecond)
print(dt_3.day_of_week)
print(dt_3.day_of_year)
print(dt_3.week_of_month)
print(dt_3.week_of_year)
print(dt_3.days_in_month)

dt_4 = pendulum.now()
#입력 받은 시간을 수정할 수도 있고, string타입으로써 출력할 수도 있다.
dt_5= dt_4.set(year=2021, month=1, day=2).to_datetime_string()
print(type(dt_5), dt_5)
print("\n")

#원하는 포멧으론 출력할 수도 있다.
dt_6 = pendulum.datetime(2022, 3, 1, 00, 00, 00)
print(dt_6.format('YYYY-MM-DD HH:mm:ss'))
print(dt_6.format('[today] dddd'))