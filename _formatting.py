#c언어 스타일의 포맷팅
name = "spidyweb"
url = "https://spidyweb.tistory.com"
print("%s의 블로그 주소는 %s 입니다. " % (name, url))

#python3부터 지원하는 format메소드 포맷팅
name = "spidyweb"
url = "https://spidyweb.tistory.com"
print("{}의 블로그 주소는 {} 입니다.".format(name, url))

#python3.6부터 지원하는 f-string 포맷팅
name = "spidyweb"
url = "https://spidyweb.tistory.com"
print(f"{name}의 블로그 주소는 {url} 입니다.")