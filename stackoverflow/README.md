### Usage:
    1. run DataCollector.py to collect data from stackoverflow api
    2. run SparkWordCounter.py to deal with data

### Current Output
it would generate top 5 votes/views tags with its content as n(1-3) grams,
output would be json file with name top_views/votes_n_grams.json, inside json file
would be [{"tag":tag, "text":[[[words], freq]]}]
```
[
  {
    "tag": "virtual-environment",
    "text": [
      [
        [
          "name",
          "ex3",
          "channels"
        ],
        10
      ],
      [
        [
          "ex3",
          "channels",
          "menpo"
        ],
        10
      ],
      [
      .......
```

    