### Usage:
    1. run DataCollector.py to collect data from stackoverflow api
    2. run SparkWordCounter.py to deal with data

### Current Output
```
+----------------+--------------------+---------------+------------------+
|             tag|  collect_list(text)|sum(view_count)|sum(up_vote_count)|
+----------------+--------------------+---------------+------------------+
|             avx|[[I was trying to...|             24|                 0|
|          render|[[[![enter image ...|             76|                 0|
|image-processing|[[Provided a phot...|             72|                 0|
| python-requests|[[I used a hooker...|              4|                 0|
|            dart|[[You can use pac...|            115|                 0|
|           azure|[[I am trying to ...|            229|                 0|
|         flutter|[[You can use pac...|            115|                 0|
|         android|[[Have tried all ...|            351|                 0|
|          java-8|[[What is the Jav...|             40|                 0|
|          celery|[[    from django...|           7476|                 6|
|           pymc3|[[I have doubts a...|             52|                 8|
|       algorithm|[[You can use `re...|             65|                 0|
|         desktop|[[Request desktop...|             65|                 0|
|           junit|[[I am trying to ...|              6|                 0|
|   numpy-ndarray|[[In a numpy arra...|             24|                 4|
|      postgresql|[[I am not sure b...|             34|                 0|
|         angular|[[It&#39;s not en...|            300|                 5|
|        firebase|[[Have tried all ...|             72|                 0|
|             oop|[[i think this sh...|             84|                 3|
|         discord|[[Currently using...|             24|                 0|
+----------------+--------------------+---------------+------------------+
only showing top 20 rows    
    