#pip install pyspark
import os
from pyspark.sql import SparkSession


os.environ['JAVA_HOME'] = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.3.2\\jbr"

filepath = "C:\\Training\\pyspark_skai\\datasets\\dw_dataset"

spark = SparkSession.builder.appName("rdd_one").master("local[*]").getOrCreate()
raw_df = spark.read.option("header", "true").option("inferSchema", "true").csv(filepath)

raw_df.show()
pd = raw_df.toPandas()
print(pd)
