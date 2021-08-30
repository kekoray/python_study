# -*- coding: utf-8 -*- 
# @Time : 2021/8/27 9:29
# @Author : koray
# @File :

from pyspark.sql import *
import pyspark.sql.functions as f
from pyspark.sql.types import StructType, StructField, StringType

session = SparkSession.builder.appName("Word Count").master("local[*]").getOrCreate()
df = session.read.csv("re_test.csv", encoding="utf-8", header=True, sep="/t", )
df.select("A").groupBy("A").count().show()

