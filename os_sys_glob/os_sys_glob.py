import os

#코로나데이터를 날짜별로 파티션한 경로로 이동
os.chdir("C:/covid19_result/partition/all_day")

#입력 경로 내의 모든 파일과 폴더명 리스트 반환
#직접 경로를 주어도 된다.
dir_list = os.listdir(".")

"""print(dir_list)

for path, direct, files in os.walk("."):
    print(path)
    print(direct)
    print(files)"""

###################################################
"""from glob import glob

print(glob("*"))
for x in glob("*"):
    if os.path.isdir(x):
        print(x,'<DIR>')
    else:
        print(x)"""
##################################################
import sys
#sys 모듈을 통해 다른 모듈이 있는 경로를 추가해준다.
sys.path.append("C:\\Users\\jiho3\\Anaconda3\\Lib\\site-packages")
#해당 venv에는 없는 모듈을 불러와서 사용할 수 있다. ex) 가상환경내에 없는 spark 모듈을 불러와 실행 시켜야 할 때 사용
import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("pyspark").getOrCreate()
spark.sql("select '#' as col1").show()

#.py 절대경로를 불러오거나, PYTHONPATH에 등록된 파이썬 모듈들이 저장된 위치를 불러온다.
#이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다.
print(sys.path)