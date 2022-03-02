import time
import datetime
#Unixtime으로 반환
print(time.time())
print("\n")

#UCT기준으로 변환하여 struct_time으로 반환
print(time.gmtime())
print("\n")

#현지 시간 기준 struct_time
print(time.localtime())
print("\n")

#struct_time을 요일 월 시간:분:초 년도 형식의 문자열로 변환 후 반환
print(time.asctime())
print("\n")

time.sleep(10)

#datetime
print(datetime.datetime.now())
print(type(datetime.datetime.now()))
print("\n")

#datetime.datetime type의 시간을 받아 원하는 포멧으로 출력하고 datetime.datetime타입으로 반환
print(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"))
print("\n")

#string type의 시간을 받아 원하는 포멧으로 출력하고 datetime.datetime타입으로 반환
print(datetime.datetime.strptime("2022-01-05 12:11:32", "%Y-%m-%d %H:%M:%S"))
print(type(datetime.datetime.strptime("2022-01-05 12:11:32", "%Y-%m-%d %H:%M:%S")))

#날짜 시간 따로, 합쳐서
d = datetime.date(2018, 7, 28)
t = datetime.time(12, 23, 38)

dt = datetime.datetime.combine(d, t)
print(dt)  # 2018-07-28 12:23:38
print("\n")
#tuple로 만들기
print(datetime.datetime.now().timetuple())

#어제, 내일 시간
now = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
yesterday = now - one_day

print(now)
print(yesterday)
print(tomorrow)