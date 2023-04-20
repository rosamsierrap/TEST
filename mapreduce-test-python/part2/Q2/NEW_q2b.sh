#!/bin/sh
../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /q2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p  /q2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../mapreduce-test-data/shot_logs.csv /q2/input/

echo "Copy and startup complete"

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper_b.py -mapper mapper_b.py \
-file reducer_b.py -reducer reducer_b.py \
-input /q2/input/* -output /q2/output/

echo "RESULTS"
/usr/local/hadoop/bin/hdfs dfs -cat /q2/output/*
