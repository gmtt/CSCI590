from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

if __name__ == '__main__':
    # read data
    raw_data = spark.read.json('raw_data.json')
    explode_tag = raw_data.withColumn('tag', explode(raw_data.tags)).drop('tags')
    union_data = explode_tag.withColumn('text', array_union('answers', array('body', 'title'))) \
        .drop('answers').drop('title').drop('body')
    group_tag = union_data.groupBy('tag').agg(collect_list('text'), sum('view_count'), sum('up_vote_count'))
    group_tag.show()
