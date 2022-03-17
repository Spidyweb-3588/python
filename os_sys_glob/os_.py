import os
#내 시스템의 환경 변수값을 알고 싶을 때
print(os.environ)
print("\n")

#현재 디렉토리 출력
print(os.getcwd())
print("\n")

#SPARK_HOME으로 디렉토리 이동
os.chdir("C:/spark/spark-3.1.2-bin-hadoop2.7")
print(os.getcwd())

#실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
#os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다.
f = os.popen("test.txt")
#읽어들인 파일 객체의 내용 보기
print(f.read())

#입력 경로 내의 모든 파일과 폴더명 리스트 반환
#직접 경로를 주어도 된다.
dir_list = os.listdir(".")
print(dir_list)