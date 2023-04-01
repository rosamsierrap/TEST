#! /usr/bin/python
import sys
import csv

for line in csv.reader(sys.stdin, quotechar='"'):
    # Registration State column is at the 3rd position
    state = line[2] 

    # Many entries have '99' as Registration state, just to provide some data cleaning we ignored those
    if (state and state != '99'):
      print('{}\t{}'.format(state, 1))