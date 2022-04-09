# 스파크가 pandas보다 느리고, 스파크는 큰 데이터가 아니면 의미없지만, 스파크에서 배운 data transformation을 활용 하기위해 스파크를 채택
# with corona가 시행됨에 따라 검사수를 더 이상 측정을 안하게됨
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from typing import Union
import findspark

findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Row
from pyspark.sql.types import StructField, StructType, DoubleType, IntegerType, TimestampType, StringType

# sparksession 드라이버 프로세스 얻기
# 이후에 나오는 mysql에 데이터 저장하기에 사용될 mysql connector jars파일을 옵션에 추가해준다.
spark = SparkSession.builder.master("local[*]").config("spark.driver.extraClassPath",
                                                       "C:/spark/spark-3.1.2-bin-hadoop2.7/jars/mysql-connector-java-8.0.28").appName(
    "pyspark").getOrCreate()

now = datetime.now()
today = date.today()
oneday = timedelta(days=1)


def getCovid19Info(start_date: date, end_date: date):
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
    api_key_utf8 = 'mrAZG1yevJBgcaaSuVLOgJ%2BS6blzA0SXlGYZrwxwpARTaMnSotfqFooTr6dgKpPcTBtE96l0xE%2B%2BmXxDrWt19g%3D%3D'
    api_key_decode = requests.utils.unquote(api_key_utf8, encoding='utf-8')

    params = {
        'serviceKey': api_key_decode,
        'startCreateDt': int('{:04d}{:02d}{:02d}'.format(start_date.year, start_date.month, start_date.day)),
        'endCreateDt': int('{:04d}{:02d}{:02d}'.format(end_date.year, end_date.month, end_date.day)),
    }

    response = requests.get(url, params=params)
    content = response.text
    elapsed_us = response.elapsed.microseconds
    print('Reqeust Done, Elapsed: {} seconds'.format(elapsed_us / 1e6))  # 100만

    return BeautifulSoup(content, "lxml")  # 불러온 text 데이터를 python xml인 lxml로 변환


# union을 통해 date, datetime 두개의 type모두 허용
def getCovid19SparkDataFrame(start_date: Union[date, datetime], end_date: Union[date, datetime]):
    # key값의 데이터 타입 정의
    convert_method = {
        'accdefrate': float,
        'accexamcnt': int,
        'createdt': lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'),
        'deathcnt': int,
        'decidecnt': int,
        'seq': int,
        'statedt': str,
        'statetime': str,
        'updatedt': lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'),
    }

    temp = getCovid19Info(start_date, end_date)
    items = temp.find('items')  # item만 추출
    item_list = []
    for item in items:
        item_dict = {}
        for tag in list(item):
            try:
                item_dict[tag.name] = convert_method[tag.name](tag.text)
            except Exception:
                item_dict[tag.name] = None
        item_list.append(item_dict)  # lxml데이터를 dictionary in list로 변환

    # dictionary의 list를 spark DataFrame으로 바꾸는 방법 dictionary 속의 key를 schema를 정의해준다.
    CovidInfo_item_Schema = StructType([
        StructField('accdefrate', DoubleType(), True),  # 누적확진률
        StructField('accexamcnt', IntegerType(), True),  # 누적의심신고검사자
        StructField('createdt', TimestampType(), True),  # 등록일시분초
        StructField('deathcnt', IntegerType(), True),  # 사망자 수
        StructField('decidecnt', IntegerType(), True),  # 확진자 수
        StructField('seq', IntegerType(), True),  # 게시글 번호(감염현황 고유값)
        StructField('statedt', StringType(), True),  # 기준일
        StructField('statetime', StringType(), True),  # 기준시간
        StructField('updatedt', TimestampType(), True)  # 수정일시분초
    ])

    df_Covid19 = spark.createDataFrame(item_list, CovidInfo_item_Schema)
    return df_Covid19


# XML로 부터 파싱된 item들의 모든 데이터를 리턴
# 데이터 조회시 메소드.show() ex)getAllCovid19Data().show()
def getAllCovid19Data():
    df_Covid19 = getCovid19SparkDataFrame(date(2019, 1, 1), now)
    print("Today: {}\nLoaded {} Records".format(now.strftime('%Y-%m-%d'), df_Covid19.distinct().count()))
    return df_Covid19


# 코로나 매일의 확진자, 누적확진자, 사망자, 누적사망자, 치명률, 검사자,누적검사자를 뽑아낸 dataframe
# 임시 선별 검사자 수는 제외(api를 못구함)
# 데이터 조회시 메소드.show() ex)getAllCovidAffectedNumbers().show()
def getAllCovidAffectedNumbers():
    from pyspark.sql import Window
    df_Covid19 = getCovid19SparkDataFrame(date(2019, 1, 1), now)
    df_Covid19_result_All = \
        df_Covid19.distinct() \
            .withColumn("decidecnt-1",
                        F.coalesce(F.lead(F.col("decidecnt"), 1).over(Window.orderBy(F.col("statedt").desc())),
                                   F.lit(0))) \
            .withColumn("deathcnt-1",
                        F.coalesce(F.lead(F.col("deathcnt"), 1).over(Window.orderBy(F.col("statedt").desc())),
                                   F.lit(0))) \
            .withColumn("기준날짜", F.from_unixtime(F.unix_timestamp(F.col("statedt"), "yyyyMMdd"), "yyyy-MM-dd")) \
            .select(F.col("기준날짜")
                    , (F.col("decidecnt") - F.col("decidecnt-1")).alias("당일확진자수")
                    , F.col("decidecnt").alias("누적확진자수")
                    , (F.col("deathcnt") - F.col("deathcnt-1")).alias("당일사망자수")
                    , F.col("deathcnt").alias("누적사망자수")
                    , F.round((F.col("deathcnt") / F.col("decidecnt") * F.lit(100)), 2).alias("전체확진자치명률(%)"))
    return df_Covid19_result_All


# 코로나 오늘의 확진자, 누적확진자, 사망자, 누적사망자, 치명률, 검사자,누적검사자를 뽑아낸 dataframe
# 임시 선별 검사자 수는 제외(api를 못구함)
# 데이터 조회시 메소드.show() ex)getAllCovidAffectedNumbers().show()
def getTodayCovidAffectedNumbers():
    from pyspark.sql import Window
    now_date = now.strftime('%Y-%m-%d')
    df_Covid19 = getCovid19SparkDataFrame(date(2019, 1, 1), now)
    df_Covid19_result_Today = \
        df_Covid19.distinct() \
            .withColumn("decidecnt-1",
                        F.coalesce(F.lead(F.col("decidecnt"), 1).over(Window.orderBy(F.col("statedt").desc())),
                                   F.lit(0))) \
            .withColumn("deathcnt-1",
                        F.coalesce(F.lead(F.col("deathcnt"), 1).over(Window.orderBy(F.col("statedt").desc())),
                                   F.lit(0))) \
            .withColumn("기준날짜", F.from_unixtime(F.unix_timestamp(F.col("statedt"), "yyyyMMdd"), "yyyy-MM-dd")) \
            .where(F.col("기준날짜") == now_date) \
            .select(F.col("기준날짜")
                    , (F.col("decidecnt") - F.col("decidecnt-1")).alias("당일확진자수")
                    , F.col("decidecnt").alias("누적확진자수")
                    , (F.col("deathcnt") - F.col("deathcnt-1")).alias("당일사망자수")
                    , F.col("deathcnt").alias("누적사망자수")
                    , F.round((F.col("deathcnt") / F.col("decidecnt") * F.lit(100)), 2).alias("전체확진자치명률(%)"))
    return df_Covid19_result_Today


# 코로나 범위내의 확진자, 누적확진자, 사망자, 누적사망자, 치명률, 검사자,누적검사자를 뽑아낸 dataframe
# 임시 선별 검사자 수는 제외(api를 못구함)
# 데이터 조회시 메소드.show() ex)getAllCovidAffectedNumbers().show()
def getPeriodCovidAffectedNumbers(start_date: Union[date, datetime], end_date: Union[date, datetime]):
    from pyspark.sql import Window
    df_Covid19 = getCovid19SparkDataFrame(date(2019, 1, 1), now)
    df_Covid19_result_Period = \
        df_Covid19.distinct() \
            .withColumn("decidecnt-1",
                        F.coalesce(F.lead(F.col("decidecnt"), 1).over(Window.orderBy(F.col("statedt").desc())),
                                   F.lit(0))) \
            .withColumn("deathcnt-1",
                        F.coalesce(F.lead(F.col("deathcnt"), 1).over(Window.orderBy(F.col("statedt").desc())),
                                   F.lit(0))) \
            .withColumn("기준날짜", F.from_unixtime(F.unix_timestamp(F.col("statedt"), "yyyyMMdd"), "yyyy-MM-dd")) \
            .where(F.col("기준날짜").between(start_date, end_date)) \
            .select(F.col("기준날짜")
                    , (F.col("decidecnt") - F.col("decidecnt-1")).alias("당일확진자수")
                    , F.col("decidecnt").alias("누적확진자수")
                    , (F.col("deathcnt") - F.col("deathcnt-1")).alias("당일사망자수")
                    , F.col("deathcnt").alias("누적사망자수")
                    , F.round((F.col("deathcnt") / F.col("decidecnt") * F.lit(100)), 2).alias("전체확진자치명률(%)"))
    return df_Covid19_result_Period, start_date, end_date  # 이후에 함수별로 저장할 때, DF가 기간으로 입력받은 것을 알기위해 기간값도 리턴


# 위의 3개의 메소드를 통해 데이터프레임을 입력받아 c드라이브 covid19_result 폴더에 함수 형태에 따른csv파일로 저장

def saveDataAsCSV(dataframe):
    if type(dataframe) == tuple:
        dataframe[0].cache()  # cache의 수명은 함수가 호출되서 끝나기까지 이므로 매 함수마다 적용
        start_date = dataframe[1]
        end_date = dataframe[2]
        if dataframe[0].count() == getPeriodCovidAffectedNumbers(start_date, end_date)[0].count():
            print("it worked!")
            return dataframe[0].coalesce(1).write.format("csv").option("header", "true").mode("overwrite").save(
                "C:/covid19_result/period/")
    else:
        dataframe.cache()
        if dataframe.count() == getAllCovidAffectedNumbers().count():  # dataframe처음 호출, 함수를 통한 dataframe처음 호출, dataframe != getAllCovidAffectedNumbers()
            print("it worked!")
            return dataframe.coalesce(1).write.format("csv").option("header", "true").mode("overwrite").save(
                "C:/covid19_result/all_day/")  # count때 호출된 dataframe이 cache된다.
        elif dataframe.count() == getTodayCovidAffectedNumbers().count():
            print("it worked!")
            return dataframe.coalesce(1).write.format("csv").option("header", "true").mode("overwrite").save(
                "C:/covid19_result/today/")


# 파티션별로 나누어 파일 저장(daily partition별로 데이터 적재)
def saveDataAsPartitionCSV(dataframe):
    if type(dataframe) == tuple:
        dataframe[0].cache()  # cache의 수명은 함수가 호출되서 끝나기까지 이므로 매 함수마다 적용
        start_date = dataframe[1]
        end_date = dataframe[2]
        if dataframe[0].count() == getPeriodCovidAffectedNumbers(start_date, end_date)[0].count():
            print("it worked!")
            return dataframe[0].write.format("csv").option("header", "true").mode("overwrite").partitionBy("기준날짜").save(
                "C:/covid19_result/partition/period/")
    else:
        dataframe.cache()
        if dataframe.count() == getAllCovidAffectedNumbers().count():
            print("it worked!")
            return dataframe.write.format("csv").option("header", "true").mode("overwrite").partitionBy("기준날짜").save(
                "C:/covid19_result/partition/all_day/")
        elif dataframe.count() == getTodayCovidAffectedNumbers().count():
            print("it worked!")
            return dataframe.write.format("csv").option("header", "true").mode("overwrite").partitionBy("기준날짜").save(
                "C:/covid19_result/partition/today/")


# mysql DB에 Covid19 DataFrame의 데이터를 저장
def saveDataToMySQL(dataframe):
    if type(dataframe) == tuple:
        dataframe[0].cache()  # cache의 수명은 함수가 호출되서 끝나기까지 이므로 매 함수마다 적용
    else:
        dataframe.cache()

    if dataframe.count() == getAllCovidAffectedNumbers().count():
        print("insert to mysql Covid19 table")
        return dataframe.coalesce(1).write.format("jdbc").options(
            url='jdbc:mysql://localhost:3306/COVID19',
            driver='com.mysql.cj.jdbc.Driver',
            dbtable='Covid_19_info',
            user='root',
            password='root'
        ).mode('overwrite').save()


if __name__ == "__main__":
    try:
        today_infection_num = (getTodayCovidAffectedNumbers().first()["당일확진자수"])
        infection_num_diff = (getTodayCovidAffectedNumbers().first()["당일확진자수"] -
                              getPeriodCovidAffectedNumbers(today - oneday, today)[0].where(
                                  F.col("기준날짜") == str(today - oneday)).first()["당일확진자수"])
        print("오늘(%s)의 확진자수는 %d명입니다.\n" % (today,
                                           today_infection_num))  # df.first()['column name'] 혹은 df.collect()[0]['column name'], 오늘의 데이터가 없을 경우 none type이 되어 에러를 낸다.try except 처리
        if infection_num_diff >= 0:
            print("어제보다 코로나 확진자가 %d명 늘었습니다.\n" % (infection_num_diff))
        else:
            print("어제보다 코로나 확진자가 %d명 줄었습니다.\n" % (-infection_num_diff))
    except TypeError:
        print("오늘의 데이터가 아직 입력되지 않았습니다.")

    saveDataAsCSV(getAllCovidAffectedNumbers())
    saveDataAsPartitionCSV(getAllCovidAffectedNumbers())
    saveDataToMySQL(getAllCovidAffectedNumbers())