target = ['  cat ', ' tiger ', '    dog', 'snake   ']

def my_key(string):
    return len(string.strip())

print(sorted(target, key=my_key))

#labmda로 표현
print(sorted(target, key=lambda x : len(x.strip())))

#map 함수
my_list = [1,2,3,4]
a = map(lambda x : x + 1,my_list)
print(list(a))