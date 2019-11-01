import json

from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def sortTags(spark):
    raw_data = spark.read.json('raw_data.json')
    explode_tag = raw_data.withColumn('tag', explode(raw_data.tags)) \
        .drop('tags').drop('answers').drop('body').drop('title').drop('up_vote_count').drop('view_count')
    group_tag = explode_tag.groupBy('tag').count().select('tag', col('count').alias('tag_count')) \
        .orderBy("count", ascending=False)
    res = group_tag.collect()
    data = []
    for row in res:
        data.append({
            'tag': row[0],
            'count': row[1]
        })
    with open('tags.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName("Word Cloud") \
        .getOrCreate()
    sortTags(spark)
