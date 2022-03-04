target = ['  cat ', ' tiger ', '    dog', 'snake   ']

def my_key(string):
    return len(string.strip())

print(sorted(target, key=my_key))

#labmda로 표현
print(sorted(target, key=lambda x : len(x.strip())))

#map 함수 1
my_list = [1,2,3,4]
a = map(lambda x : x + 1,my_list)
print(list(a))

#map 함수 예제 2
my_list2 = ["a", "b", "c", "d"]
b = map(lambda y: y.upper(), my_list2)
print(list(b))

#filter 함수 예제
result = list(filter((lambda x: x % 2 == 1), range(20)))
print(result)
