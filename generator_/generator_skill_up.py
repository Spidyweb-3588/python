#함수 안에 return 키워드 대신에 yield 키워드를 사용하여 만듦
def generator():
    yield 1
    yield 3
    yield 5
    yield 'a'

#generator 생성
gen = generator()

print(type(gen))# <class 'generator'> 출력
print(next(gen))# 1출력
print(gen.__next__())# 다음과 같은 방법으로도 출력이 가능하다. 3출력
print(next(gen))# 5출력
print(next(gen))# a출력
#print(next(gen)) StopIteration출력

#위의 함수는 iterable로 부터 iterator를 생성하는 다음 코드와 같다.
iterable_list = [1,3,5,'a']
iterator_list = iter(iterable_list)
print(type(iterator_list))# <class 'generator'> 출력
print(next(iterator_list))# 1출력
print(next(iterator_list))# 3출력
print(next(iterator_list))# 5출력
print(next(iterator_list))# a출력
#print(next(iterator_list)) StopIteration출력

#또 다른 generator 생성
gen2 = generator()

#생성한 두 개의 generator는 서로 다르다.
print(gen==gen2) #False출력
print(gen is gen2) #False출력

###################################################

#n범위에 각각 1을 더하는 제너레이터
def add_one(n):
    for num in range(n):
        yield num+1

gen3 = add_one(10)
print(type(gen3)) #<class 'generator'>출력

for i in gen3:
    print(i)

#위의 제너레이터를 일반 함수로 구현
def add_one_normal(n):
    lst = []
    for num in range(n):
        lst.append(num+1)
    return lst

fnc = add_one_normal(10)
for i in fnc:
    print(i)

