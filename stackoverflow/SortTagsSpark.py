from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import pyspark.sql.functions as f

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

if __name__ == '__main__':
    raw_data = spark.read.json('raw_data.json')
    explode_tag = raw_data.withColumn('tag', explode(raw_data.tags)) \
        .drop('tags').drop('answers').drop('body').drop('title').drop('up_vote_count').drop('view_count')
    group_tag = explode_tag.groupBy('tag').count().select('tag', f.col('count').alias('tag_count'))\
        .orderBy("count", ascending=False).show()

    # tag_list = explode_tag.collect()
    # tag_array = []
    # for i in range(0, len(tag_list)-1) :
    #     tag_array.append(tag_list[i].tag)
    # tag_array.show()









