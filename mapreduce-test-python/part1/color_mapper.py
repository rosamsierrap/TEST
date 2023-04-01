#! /usr/bin/python
import sys
import csv

for line in csv.reader(sys.stdin, quotechar='"'):
    # Color column is at the 34th position
    color = line[33] 

    # If color data is found
    if (color):
      print('{}\t{}'.format(color, 1))


