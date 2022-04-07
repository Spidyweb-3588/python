from glob import glob
import os

#현재 디렉토리 변경
os.chdir("C:\python_skillup")

#현재 경로의 모든 디렉토리,파일을 출력(숨긴 파일은 출력x)
print(glob("*"))
print("\n")
#현재 경로의 모든 디렉토리,파일을 출력(숨긴 파일도 출력o)
print(os.listdir("."))
print("\n")

#해당 경로의 모든 디렉토리,파일을 출력
print(glob("C:/python_skillup/os_sys_glob/*"))

#해당 경로의 모든 .py파일 출력
print(glob("C:/baekjoon_algorithm/*.py"))

#현재 디렉토리의 모든 디렉토리,파일을 불러와 디렉토리일 경우 <DIR>를 붙여 출력하고 디렉토리가 아닐경우 그냥 출력
for x in glob("*"):
    if os.path.isdir(x):
        print(x,'<DIR>')
    else:
        print(x)