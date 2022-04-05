a = [1,2,3]
b = set()
c = "str"
d = dict()
e = tuple()
f = range(1,3)

#print(a.__next__) AttributeError: 'list' object has no attribute '__next__'
#print(b.__next__) AttributeError: 'set' object has no attribute '__next__'
#print(c.__next__) AttributeError: 'str' object has no attribute '__next__'
#print(d.__next__) AttributeError: 'dict' object has no attribute '__next__'
#print(e.__next__) AttributeError: 'tuple' object has no attribute '__next__'
#print(f.__next__) AttributeError: 'range' object has no attribute '__next__'
#위의 6개 타입은 iterable이며, iterator가 아니다.

print(type(a))
a = iter(a)
print(type(a))
print(a.__next__())#1출력
print(a.__next__())#2출력
print(a.__next__())#3출력
#print(a.__next__())#StopIteration출력

################################################################################

#Iterable한 객체를 만들 수 있는 클래스
class Iterable:
    def __init__(self, start_number, stop_number):
        self.start_number = start_number #시작 값
        self.stop_number = stop_number # 종료 값

    def __iter__(self):
        return Iterator(self.start_number, self.stop_number)

class Iterator:
    def __init__(self, start_number, stop_number):
        self.start_number = start_number #시작 값
        self.current_number = start_number #현재 값
        self.stop_number = stop_number  # 종료 값

    def __next__(self):
        if self.current_number < self.stop_number:
            self.current_number += 1
            return self.current_number
        else:
            raise StopIteration

test = Iterable(5,20).__iter__() #test를 iterable 인스턴스로 만든 후 __iter__메소드 호출
print(type(test))
for i in range(5,25):
    try:
        print(test.__next__())
    except:
        print("StopIteration 발생")

#########################################################################################
#iterable과 iterator를 같이 구현한 class
class IterableAndIterator:
    def __init__(self, start_number, stop_number):
        self.stop_number = start_number # 시작 값 지정
        self.stop_number = stop_number # 종료 값 지정
        self.current_number = start_number # 현재 값 지정

    def __iter__(self):
        return self # 자기 자신 객체를 리턴

    def __next__(self):
        if self.current_number < self.stop_number:
            self.current_number += 1
            return self.current_number
        else:
            raise StopIteration

test2 = IterableAndIterator(5,20)
print(type(test2))
for i in range(5,25):
    try:
        print(test2.__next__())
    except:
        print("StopIteration 발생")
