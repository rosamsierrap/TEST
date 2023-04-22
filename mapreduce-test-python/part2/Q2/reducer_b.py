#!/usr/bin/python
# ---- coding:utf-8 ----
import random
import sys
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("PART12")
sc = SparkContext(conf=conf)

textFile = sc.textFile(sys.argv[1]) #data
info = textFile.flatMap(lambda line: line.split("\t")) #line

p = info.map(lambda line: (line.split(",")[0],  #player
            (eval(line.split(",")[1]),  #data
            )) \
         .groupByKey() \
         .mapValues(list) \
         .collectAsMap()

cntd = 4
cntds = {}

def l2(set1, set2):  #DONE
    d = 0
    for i in range(len(set1)):
        d += (set1[i] - set2[i]) ** 2
    return( ** 0.5)
#########################
             
             
             
 #####

for player,data in p.items():
    if len(data) < 4:
        continue
    # Initialize centroids 
    if player not in cntds:
        cntds[player]=[]
    if not cntds[player]:
        nums = []
        for _ in range(cntd):
            nums.append(random.randint(0,len(data)-1))
            if len(nums)==1:
                continue
            while nums[-1] == nums[-2]:
                nums[-1] = random.randint(0,len(data)-1)
        for i in nums:
            cntds[player].append(data[i])
    # calc closest distances
    for _ in range(10):
        future_centroid = []
        for k in range(cntd):
            future_centroid.append([])
        for dataset in data:
            distances = []
            for centroid_positions in cntds[player]:
                dst = l2(centroid_positions,dataset)
                distances.append(dst)
            min_indx = -1
            min_val = 100000
            j=0
            for k in distances:
                if k < min_val:
                    min_val = k
                    min_indx = j
                j+=1
            future_centroid[min_indx].append(dataset)
        for ix,f_cntd in enumerate(future_centroid):
            d = []
            t=0
            try:
                for t in range(len(f_cntd[0])):
                    d.append(0)
                for row in f_cntd:
                    for k,point in enumerate(row):
                        d[k] += point
                    t +=1
                for indx,point in enumerate(d):
                    d[indx] = round(d[indx]/t,4)
                future_centroid[ix] = d
            except:
                pass
        for i in range(len(cntds[player])):
            if future_centroid[i]:
                cntds[player][i] = future_centroid[i]

for player,centroid_pos in cntds.items():
    print(player+'\t'+str(centroid_pos))
