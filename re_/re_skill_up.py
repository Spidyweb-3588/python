import re

#1. match객체
text = "abc"
text2 = "3 python"

p = re.compile('[a-z]+')
m = p.match(text)
n = p.match(text2)
print(m)
#<re.Match object; span=(0, 3), match='abc'> 출력
print(n)
#None 출력
if m:
    print('Match found: ', m.group())
else:
    print('No match')
#Match found: abc 출력
if n:
    print('Match found: ', m.group())
else:
    print('No match')
#No match 출력

#Match 객체의 메소드
print(m.group(),m.start(),m.end(),m.span())
#abc, 0, 3, (0,3) 출력


#2. search객체
a = p.search(text)
print(a)
#<re.Match object; span=(0, 3), match='abc'> 출력
b = p.search(text2)
print(b)
#<re.Match object; span=(2, 8), match='python'> 출력

#3. findall객체
text3 = "life is too short"
q = p.findall(text3)
print(q)
#['life', 'is', 'too', 'short'] 출력


#4. finditer객체
w = p.finditer(text3)
print(w)
#<callable_iterator object at 0x000001A3A8388400> 출력
for i in w:
    print(i)
#<re.Match object; span=(0, 4), match='life'>
#<re.Match object; span=(5, 7), match='is'>
#<re.Match object; span=(8, 11), match='too'>
#<re.Match object; span=(12, 17), match='short'>

#5. 컴파일 옵션
p = re.compile("string",re.MULTILINE)#re.compile(텍스트, 컴파일옵션) 과 같이 사용한다.

#6. 백슬래쉬와 Raw String 규칙
#\t\n\r\f\v 와 같이 white space에 대해서는 정규식을 적용하고 싶다면 \를 2번 사용
p = re.compile('\\nowhitespace')
print(p.search('example\nowhitespace'))
#<re.Match object; span=(7, 19), match='\nowhitespace'> 출력

p = re.compile('\\\\nowhitespace')
print(p.search('example\\nowhitespace'))
#<re.Match object; span=(7, 20), match='\\nowhitespace'> 출력

p = re.compile(r'\nowhitespace')
print(p.search('example\nowhitespace'))
#<re.Match object; span=(7, 20), match='\nowhitespace'> 출력

#7. 그룹핑
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")#이름 + " " + 전화번호 형태의 문자열을 찾는 정규식
m = p.search("park 010-1234-1234")

#이름만 뽑아내는 정규식
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")#0번 째 그룹은 park 010-1234-1234, 1번 째 그룹은 park이다.
m = p.search("park 010-1234-1234")
print(m.group(1))#park 출력

#이름과 전화번호를 그룹핑하는 정규식
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(1),m.group(2))#park 010-1234-1234 출력

#이름과 전화번호와 국번만 뽑아내는 정규식
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")#2번 째 그룹 안에 중첩된 그룹을 만들 수 있다(3번 째 그룹)
m = p.search("park 010-1234-1234")
print(m.group(1), m.group(2), m.group(3))#park 010-1234-1234 010 출력

#그룹핑 문자열 재참조
p = re.compile(r'(\b\w+)\s+\1')#(\b\w+)\s+\1은 (그룹) + " " + 그룹과 동일한 단어, 2개의 동일한 단어를 연속적으로 사용해야만 매치
m = p.search('hello python python python bye')
print(m.group())#python python 출력

#그룹핑 문자열에 이름 붙이기
p = re.compile(r'(?P<myfirstgroup>\w+)\s+((\d+)[-]\d+[-]\d+)')#\w에 첫번째 그룹핑이 되어 myfirstgroup이라는 그룹명을 부여
m = p.search("park 010-1234-1234")
print(m.group("myfirstgroup"))

#그룹핑 문자열 이름 붙여 재참조
p = re.compile(r'(?P<myfirstgroup>\b\w+)\s+(?P=myfirstgroup)')#그룹핑 명에 이름을 부여하면 (?P=그룹핑 명) 처럼 사용하여 재참조한다.
m = p.search("hello python python python bye")
print(m.group())#python python 출력

#전방형 탐색
#.*[.](?!bat$).*$ #확장자가 bat가 아닌 경우에만 통과된다는 의미
#.*[.](?!bat$|exe$).*$ #확장자가 bat이거나 exe이면 제외하라는 조건

#문자열 변환 sub 메소드
p = re.compile(r'(score|password|grade)')
m = p.sub('encoding target','your score, password, grade, name, telephone is here')#1번째 매개변수자리엔 변환할 문자열, 2번째 문자열엔 적용 대상 문자열
print(m)#your encoding target, encoding target, encoding target, name, telephone is here 출력

m = p.sub('encoding target','your score, password, grade, name, telephone is here',count=1)#맨 앞의 1개만 변환
print(m)#your encoding target, password, grade, name, telephone is here 출력

m = p.subn('encoding target','your score, password, grade, name, telephone is here',2)#맨 앞의 2개만 변환하여 튜플로 출력
print(m)#('your encoding target, encoding target, grade, name, telephone is here', 2) 출력
