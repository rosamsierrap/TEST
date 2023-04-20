#!/bin/sh
../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /q2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p  /q2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../mapreduce-test-data/shot_logs.csv /q2/input
echo "Copy and startup complete"
