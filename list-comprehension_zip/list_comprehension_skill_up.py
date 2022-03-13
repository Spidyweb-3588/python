# list를 만들고 값을 입력하는 일반적인 방법
numbers = []
for n in range(0, 10):
    numbers.append(n)
print(numbers)
print("\n")

# list comprehension을 통해 list를 만듦과 동시에 값을 입력하는 방법
numbers_2 = [x for x in range(10)]
print(numbers_2)
print("\n")

# list comprehension 문법 예제 2 입력될 값에 곱하기
"""
#이 코드는 아래와 같이 바꾸어 사용할 수 있다.
numbers_3 = []
for x in range(0, 10):
    numbers_3.append(x*2)
print(numbers_3)
"""
numbers_3 = [x*2 for x in range(10)]
print(numbers_3)
print("\n")

# list comprehension 문법 예제 3 리스트에 함수를 적용하여 새로운 list 생성
"""
#이 코드는 아래와 같이 바꾸어 사용할 수 있다.
names = ["SPIDY","WEB"]
lower_names = []
for i in names:
    lower_names.append(i.lower())
print(lower_names)
"""
names = ["SPIDY","WEB"]
lower_names = [name.lower() for name in names]
print(lower_names)
print("\n")

#list comprehension 그리고 set comprehension 결과값 비교
#set는 중복된 값을 표현하지 않는다.
print([x+y for x in range(10) for y in range(10)])
print({x+y for x in range(10) for y in range(10)})
print("\n")

# dictionary comprehension 예제 1, 리스트를 키로, value로 0을 입력
students = ['철수', '영희', '길동', '순희']
print({student: 0 for student in students})
print("\n")

# dictionary comprehension 예제 2, 리스트 2개를 zip으로 묶어 x를 key로 y를 value로 입력
scores = [50,60,80,90]
dict_compre = {x:y for x, y in zip(students,scores)}
print(dict_compre)
print("\n")

# dictionary comprehension 예제 3, 기존의 dictionary로 부터 새로운 dictionary 생성(자신의 점수 - 평균점수)
scores_1 = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
print({name: score-sum(scores_1.values())/len(scores_1) for name, score in scores_1.items()})
