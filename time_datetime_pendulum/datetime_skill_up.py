from datetime import timedelta, timezone, date, datetime, time

def print_datetime():
    print(datetime(2022, 3, 2))
    print(datetime(2022, 3, 2, 13, 25, 23))
    #현재시간 출력
    print(datetime.now())
    #현재시간얻는 메소드 타입 출력
    print(type(datetime.now()))
    print("\n")

    # datetime.datetime type의 시간을 받아 원하는 포멧으로 출력하고 str타입으로 반환
    print(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))
    print(datetime.strftime(datetime(2022, 3 ,1), "%Y-%m-%d %H:%M"))
    print(type(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")))
    print("\n")

    # string type의 시간을 받아 원하는 포멧으로 출력하고 datetime.datetime타입으로 반환
    print(datetime.strptime("2022-01-05 12:11:32", "%Y-%m-%d %H:%M:%S"))
    print(type(datetime.strptime("2022-01-05 12:11:32", "%Y-%m-%d %H:%M:%S")))
    print("\n")
    #datetime, date, time 클래스에서 모두 지원하는 strftime() 메서드와 달리 strptime() 메서드는 datetime 클래스에서만 지원
    print(datetime.now().timetuple())
    print(type(datetime.now().timetuple()))
    print("datetime 마지막 줄\n")

def print_date():
    print(date(2022, 3, 2))
    print("\n")
    #오늘 날짜 출력
    _today = date.today()
    print(_today)
    print("\n")
    #오늘 날짜의 년,월,일 각각 출력
    print(_today.year)
    print(_today.month)
    print(_today.day)
    print("\n")
    #datetime.date의 날짜를 받아 str으로 변환
    print(type(_today.isoformat()), _today.isoformat())
    #string type의 날짜를 받아 datetime.date로 변환
    print(type(date.fromisoformat('2022-03-02')), date.fromisoformat('2022-03-02'))
    print("date 마지막 줄\n")

def print_time():
    #입력한 시간을 datetime.time으로 출력
    print(type(time(13, 24, 30)), time(13, 24, 30))
    #아무것도 입력안할 시 00:00:00 출력
    print(time())
    #HH:MM:SS.ffffff 형태의 문자열을 time객체로 반환
    print(time.fromisoformat('13:22:12.234+09:00'))

    t = time(9, 22, 55, 458000, tzinfo=timezone(timedelta(hours=9)))
    #time 객체를 문자열로 반환
    print(type(t.isoformat()), t.isoformat())
    print(t.hour, t.minute, t.second, t.microsecond)
    print(t.replace(hour=2,second=46, tzinfo=timezone(timedelta(hours=4))))
    print(t.tzinfo)
    # 어제, 내일 시간
    now = datetime.now()
    one_day = timedelta(days=1)
    tomorrow = now + one_day
    yesterday = now - one_day
    print(yesterday)
    print(now)
    print(tomorrow)
    # 날짜 시간 따로, 합쳐서
    d = date(2018, 7, 28)
    t = time(12, 23, 38)

    dt = datetime.combine(d, t)
    print(dt)  # 2018-07-28 12:23:38
    print("time 마지막 줄 \n")

if __name__=='__main__':
    print_datetime()
    print_date()
    print_time()