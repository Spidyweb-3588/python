import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window

#sparksession 드라이버 프로세스 얻기
spark = SparkSession.builder.appName("sample").master("local[*]").getOrCreate()

df_crash = spark.read.format("csv").option("header","true").option("inferschema","true").load("C:/Users/jiho3/Downloads/Motor_Vehicle_Collisions_-_Crashes.csv")

df_crash_losses = df_crash \
    .withColumn("CRASH_DATE_FORMATTED",
                F.from_unixtime(F.unix_timestamp(F.col("CRASH DATE"), "MM/dd/yyyy"), "yyyy/MM/dd")) \
    .withColumn("CRASH_TIME_HH", F.lpad(F.col("CRASH TIME"), 5, "0")) \
    .where(F.col("CRASH_TIME_HH").between("00:00", "06:00") & F.col("BOROUGH").isin("MANHATTAN")) \
    .groupBy(F.col("CRASH_DATE_FORMATTED"), F.col("CRASH_TIME_HH")) \
    .agg(F.max(F.col("NUMBER OF PERSONS INJURED")).alias("TOTAL_INJURED")
         , F.max(F.col("NUMBER OF PERSONS KILLED")).alias("TOTAL_KILLED"))

# 날짜별 부상자 숫자 순위를 메기는 컬럼과 날짜별 사망자 숫자 순위를 메기는 컬럼을 생성해서 날짜별 부상자수가 1위거나 사망자수가 1위인 시간,날짜,컬럼조회
df_crash_or = df_crash_losses \
    .withColumn("MAX_INJURED_DESC_RN", F.row_number().over(
    Window.partitionBy(F.col("CRASH_DATE_FORMATTED")).orderBy((F.col("TOTAL_INJURED"))))) \
    .withColumn("MAX_KILLED_DESC_RN",
                F.row_number().over(Window.partitionBy(F.col("CRASH_DATE_FORMATTED")).orderBy((F.col("TOTAL_KILLED"))))) \
    .where((F.col("MAX_INJURED_DESC_RN") <= 1) | (F.col("MAX_KILLED_DESC_RN") <= 1)) \
    .select(F.col("CRASH_DATE_FORMATTED")
            , F.col("CRASH_TIME_HH")
            , F.col("TOTAL_INJURED")
            , F.col("TOTAL_KILLED")) \
    .orderBy(F.col("CRASH_DATE_FORMATTED")
             , F.col("CRASH_TIME_HH"))


print(df_crash_losses.count())
spark.stop()