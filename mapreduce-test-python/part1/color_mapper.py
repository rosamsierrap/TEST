#! /usr/bin/python
import sys
import csv

for line in csv.reader(sys.stdin, quotechar='"'):
    # Color column is at the 34th position
    color = line[33] 

    # If color data is found
    if (color):
      if color in ("GY","GRAY", "GRY", "GREY", "Gray"):
        color = "GRAY"
      elif color in ("BLK","BK","BLACK"):
        color = "BLACK" 
      elif color in ("WH","WHITE", "WHT", "WHI"):
        color = "WHITE" 
      elif color in ("SILVE","SLVR","SIL"):
        color = "SILVER"
      elif color in ("GREEN","GRN","GREN"):
        color = "GREEN" 
      elif color in ("YW","YELLO"):
        color = "YELLOW" 
      elif color in ("BLUE", "BLU"):
        color = "BLUE" 
      elif color in ("RED", "RD"):
        color = "RED" 
        
      print('{}\t{}'.format(color, 1))


