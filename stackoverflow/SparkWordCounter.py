import collections
import json
import re
import string

from nltk.util import ngrams
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

FILTER_LIST = ['the', 'I', 'an', 'to']


def word_count(row, freq):
    tag = row.tag
    text = map(lambda strs: "\n".join(strs), row.text)
    text = "\n".join(text)
    # get rid of punctuation (except periods!)
    punctuationNoPeriod = "[" + re.sub("\.", "", string.punctuation) + "]"
    text = re.sub(punctuationNoPeriod, "", text)

    tokenized = text.split()
    esBigrams = ngrams(tokenized, freq)

    if freq == 1:
        text = collections.Counter(filter(filter_single_word, esBigrams)).most_common(100)
    else:
        text = collections.Counter(esBigrams).most_common(100)
    return {'tag': tag, 'text': text}


def filter_single_word(t):
    if t[0] in FILTER_LIST:
        return False
    return True


if __name__ == '__main__':
    # read data
    raw_data = spark.read.json('raw_data.json')
    explode_tag = raw_data.withColumn('tag', explode(raw_data.tags)).drop('tags')
    union_data = explode_tag.withColumn('text', array_union('answers', array('body', 'title'))) \
        .drop('answers').drop('title').drop('body')
    group_tag = union_data.groupBy('tag') \
        .agg(collect_list('text').alias('text'),
             sum('view_count').alias('view_count'),
             sum('up_vote_count').alias('up_vote_count'))
    top_views = group_tag.sort('view_count', ascending=False).limit(5)
    for i in range(1, 4):
        res = top_views.rdd.map(lambda x: word_count(x, i)).collect()
        with open('top_views_{}_grams.json'.format(i), 'w') as out:
            json.dump(res, out)
    top_votes = group_tag.sort('up_vote_count', ascending=False).limit(5)
    for i in range(1, 4):
        res = top_votes.rdd.map(lambda x: word_count(x, i)).collect()
        with open('top_votes_{}_grams.json'.format(i), 'w') as out:
            json.dump(res, out)
