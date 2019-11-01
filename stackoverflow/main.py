"""
this script accepts two parameters:
    1. site name like stackoverflow
    2. page size

example:
    python main.py stackoverflow 10

"""
import sys
from pyspark.sql import SparkSession

from DataCollector import fetch
from SortTagsSpark import sortTags
from SparkWordCounter import spark_process
from stackapi import StackAPI

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("not enough arguments!")
        exit(1)
    site_name = sys.argv[1]
    page_size = sys.argv[2]

    # initialize spark
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .getOrCreate()

    # collect data
    fetch(StackAPI(site_name), page_size)

    # sort tags
    sortTags(spark)

    # word count
    spark_process(spark)