#내부함수를 결과로 반환 하는 함수가 있을 때, 내부 함수를 closure라고 한다.
def add(x, y):
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add

#함수에 로깅을 추가해주는 wrapper함수를 closure함수로 만든다.
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

#wrapper함수를 decorator를 이용하여 다른 함수에 적용
@logged
def add(x,y):
    return x + y

print(add(1,3))
#calling add
#4 출력
########################################

#정적 메소드는 클래스에 속한 함수지만 인스턴스에 대해 연산하지 않음
class Foo(object):
    @staticmethod
    def bar(x):
        print('x =', x)

Foo.bar(2)
# x = 2 출력

#클래스 메소드
class Poo:
    def bar(self):
        print(self)

    @classmethod
    def spam(cls):
        print(cls)

p = Poo()
p.bar()
Poo.spam()

#클래스 메소드 2
import time
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        # 클래스가 어떻게 인자로 전달되는지 보라
        tm = time.localtime()
        # 새 인스턴스를 생성하는 데 사용됨
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
print(d.year)
print(d.month)
print(d.day)

#@property는 메소드를 마치 속성처럼 사용할 수 있게 해줌
class Car:
    def __init__(self, model):
        self.model = model

    @property
    def get_model(self):
        return self.model

c = Car("GV80")
print(c.get_model)          # c.get_model()이 아님 GV80출력
