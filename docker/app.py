from pyspark.sql import SparkSession


spark = SparkSession.builder\
                    .getOrCreate()

df = spark.read.csv("/mnt/vvdevdsdatalake/iris.csv", header=True)
df.show()

spark.stop()
