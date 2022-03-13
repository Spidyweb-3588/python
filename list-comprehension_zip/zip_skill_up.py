list_1 = ["a","b","c","d"]
list_2 = [1,2,3,4,5,6,7]

#list 2개를 묶어 새로운 tuple들의 list 생성
new_list = list(zip(list_1, list_2))
print(new_list)
print("\n")

#tuple들의 list는 각 값을 출력할 수 있다.
for n, p in zip(list_1, list_2):
    print(n,p)
print("\n")

#zip을 이용하여 list 2개를 묶고 dictionary로써 생성할 수도 있다.
new_dict = dict(zip(list_1, list_2))
print(new_dict)
print("\n")

tuple_1 = (1,2,3)
tuple_2 = ("a","b","c","d")
#튜플들을 묶어 새로운 튜플 생성
new_tuple = tuple(zip(tuple_1, tuple_2))
print(new_tuple)
#((1, 'a'), (2, 'b'), (3, 'c')) 출력
print("\n")

#리스트와 튜플을 묶어 리스트로 변환도 가능
list_of_tuple = list(zip(list_1,tuple_1))
print(list_of_tuple)
#[('a', 1), ('b', 2), ('c', 3)] 출력
print("\n")

dict_1 = {"abc":123,"def":456,"ghi":789}
dict_2 = {"a":1,"b":2,"c":3}
#dictionary들을 묶어 새로운 dictionary생성 가능 {dictionary1.keys(), dictionary2.keys()}와 같다.
dict_of_dict = dict(zip(dict_1, dict_2))
print(dict_of_dict)
#{'abc': 'a', 'def': 'b', 'ghi': 'c'} 출력
print("\n")

#dictionary들을 묶어 새로운 dictionary생성 가능 {dictionary1.keys(), dictionary2.values()}와 같다.
dict_of_dict2 = dict(zip(dict_1.keys(), dict_2.values()))
print(dict_of_dict2)
#{'abc': 1, 'def': 2, 'ghi': 3} 출력
print("\n")

#dictionary들을 묶어 새로운 dictionary생성 가능 {dictionary1.items(), dictionary2.items()}와 같다.
dict_of_dict3 = dict(zip(dict_1.items(), dict_2.items()))
print(dict_of_dict3)
#{('abc', 123): ('a', 1), ('def', 456): ('b', 2), ('ghi', 789): ('c', 3)} 출력