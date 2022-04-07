import sys
#sys 모듈을 통해 다른 모듈이 있는 경로를 추가해준다.
sys.path.append("C:/Users/user/Anaconda3/Lib/site-packages")
#해당 venv에는 없는 모듈을 불러와서 사용할 수 있다. ex) 가상환경내에 없는 spark 모듈을 불러와 실행 시켜야 할 때 사용
import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("pyspark").getOrCreate()
spark.sql("select '#' as col1").show()

#.py 절대경로를 불러오거나, PYTHONPATH에 등록된 파이썬 모듈들이 저장된 위치를 불러온다.
#이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다.
print(sys.path)

#명령 행에서 인수 전달하기
#명령프롬프트 창에서 현재 파이썬파일 이후에 인수를 전달하면 sys.argv에 list로써 인수들이 저장된다.
print(sys.argv)