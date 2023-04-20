#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("PART1")
sc = SparkContext(conf=conf)

textFile = sc.textFile(sys.argv[1]) #data

info = textFile.flatMap(lambda line: line.split("\n")) #lines

ShotDistDefdistTime= info.map(lambda line: (line.split(",")[15]+line.split(",")[16].strip('"'),  #shooter
                                            (float(line.split(",")[12]),  #dist
                                             float(line.split(",")[18]), #def_dist
                                             float(line.split(",")[9])))) #time

made = ShotDistDefdistTime.filter(lambda pair: pair[1][0] == 'made') #hit==made

made_byshooter = made.groupByKey()

p = made_byshooter.map(lambda pair: (pair[0], list(pair[1]))).collectAsMap()

output = sc.parallelize([shooter+'\t'+str(info) for shooter,info in p.items()])
output.saveAsTextFile("output.txt")

sc.stop()
                      
