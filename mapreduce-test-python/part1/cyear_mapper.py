#! /usr/bin/python
import sys
import csv

for line in csv.reader(sys.stdin, quotechar='"'):
    # Year column is at the 36th position
    year = line[35] 

    # Many entries have 0 as year, just to provide some data cleaning we ignored those
    if (year != '0'):
      print('{}\t{}'.format(year, 1))
