from pyspark.sql import SparkSession
import pandas as pd
from collections import Counter, OrderedDict
import json
from pyspark.sql.functions import *

# spark = SparkSession \
#     .builder \
#     .appName("Python Spark SQL basic example") \
#     .getOrCreate()

if __name__ == '__main__':
    # df = spark.read.json('raw_data.json')
    # df.printSchema()
    df = pd.read_json('raw_data.json')
    ser = pd.Series(df['tags'])
    # print(ser.head(10))
    # df2 = pd.DataFrame(columns=['tag'])
    df2 = []
    for s in ser :
        a = [[x] for x in s]

        # print(a)
        for a1 in a:
            # print(a1)
            df2.append(tuple(a1))

    # print(df2)


    # count_map = {}
    # for i in df2 :
    #     count_map[i] = count_map.get(i, 0) + 1
    # print(count_map)
    dictionary_tag = Counter(df2)
    print(dictionary_tag)
    print(dictionary_tag.most_common(5))

    sorted_dict = OrderedDict(sorted(dictionary_tag.items(), key = lambda kv : kv[1], reverse=True))
    with open('result.json', 'w') as out:
        for v in sorted_dict :
            print(v[0], sorted_dict[v])
            json.dump((v[0], sorted_dict[v]), out)


    # a = df.select("tags")
    # print()
    # for a1 in a :
    #     a1.show()
    #new_df = spark.read.json(df.rdd.map(lambda r : r.json))
    #new_df.printSchema()