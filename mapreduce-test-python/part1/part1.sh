#! /bin/sh
#! /usr/bin/python
../../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /p1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /p1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /p1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/nyc_parking_violations_data.csv /p1/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar  \
-file ../../mapreduce-test-python/part1/hour_mapper.py -mapper ../../mapreduce-test-python/part1/hour_mapper.py \
-file ../../mapreduce-test-python/part1/reducer.py -reducer ../../mapreduce-test-python/part1/reducer.py \
-input /p1/input/* -output /p1/output/Q1

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar  \
-file cyear_mapper.py -mapper cyear_mapper.py \
-file reducer.py -reducer reducer.py \
-input /p1/input/* -output /p1/output/Q2/car_year

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar  \
-file ctype_mapper.py -mapper ctype_mapper.py \
-file reducer.py -reducer reducer.py \
-input /p1/input/* -output /p1/output/Q2/car_type

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar  \
-file state_mapper.py -mapper state_mapper.py \
-file reducer.py -reducer reducer.py \
-input /p1/input/* -output /p1/output/Q3/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar  \
-file color_mapper.py -mapper color_mapper.py \
-file reducer.py -reducer reducer.py \
-input /p1/input/* -output /p1/output/Q4/

echo "--------------------------- Question 1: At what hour of the day are tickets most likely to be issued? ---------------------------" 
/usr/local/hadoop/bin/hdfs dfs -cat /p1/output/Q1/part-00000

echo "--------------------------- Question 2.1: Most common year to be ticketed ---------------------------" 
/usr/local/hadoop/bin/hdfs dfs -cat /p1/output/Q2/car_year/part-00000

echo "--------------------------- Question 2.2: Most common type to be ticketed ---------------------------" 
/usr/local/hadoop/bin/hdfs dfs -cat /p1/output/Q2/car_type/part-00000

echo "--------------------------- Question 3: Most common state to be ticketed (where) ---------------------------" 
/usr/local/hadoop/bin/hdfs dfs -cat /p1/output/Q3/part-00000

echo "--------------------------- Question 4: Most common color to be ticketed ---------------------------" 
/usr/local/hadoop/bin/hdfs dfs -cat /p1/output/Q4/part-00000


/usr/local/hadoop/bin/hdfs dfs -rm -r /p1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /p1/output/

../../stop.sh
