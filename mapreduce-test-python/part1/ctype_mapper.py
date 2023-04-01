#! /usr/bin/python
import sys
import csv

for line in csv.reader(sys.stdin, quotechar='"'):
    # Type column is at the 7th position
    car_type = line[6]
    if car_type:

        # If we find data for the data point we map it to 1
        print('{}\t{}'.format(car_type, 1))
