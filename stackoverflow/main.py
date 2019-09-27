from pprint import pprint
from stackapi import StackAPI
from pyspark import SparkConf, SparkContext
from pyspark.sql import Row, SQLContext
from pyspark.streaming import StreamingContext


SITE = StackAPI('stackoverflow')
my_questions = []
PAGE_SIZE = 50

for page in range(1,10):
    questions = SITE.fetch('/questions',
                           filter='!*7PmgXSIwIci20AhfbtbTX7Oz()A',
                           page=page,
                           pagesize=PAGE_SIZE)

    for question in questions['items']:
        my_question = {
            'tags': question['tags'],
            'title': question['title'],
            'body': question['body_markdown'],
            'answers': []
        }
        if 'answers' in question:
            for answer in question['answers']:
                my_question['answers'].append(answer['body_markdown'])
        my_questions.append(my_question)

#pprint(my_questions)

# config
conf = SparkConf()
conf.setAppName("TwitterStreamApplication")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 1)
ssc.checkpoint("checkpoint_TwitterStreamApp")


