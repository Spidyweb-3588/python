numbers = []
for n in range(0, 10):
    numbers.append(n)
print(numbers)
###다음과 같다
numbers_2 = [x for x in range(10)]
print(numbers_2)

numbers_3 = [x*2 for x in range(10)]
print(numbers_3)

names = ["SPIDY","WEB"]
lower_names = [name.lower() for name in names]
print(lower_names)

print([x+y for x in range(10) for y in range(10)])
print({x+y for x in range(10) for y in range(10)})

students = ['철수', '영희', '길동', '순희']
scores = [50,60,80,90]
print({student: 0 for student in students})
print("\n")

dict_compre = {x:y for x, y in zip(students,scores)}
print(dict_compre)


scores_1 = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
print({name: score for name, score in scores_1.items()})