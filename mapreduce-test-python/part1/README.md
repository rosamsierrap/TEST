# NYC Parking and Tickets Analysis (Part 1)

This repository contains five different mapper scripts and one common reducer script to answer four different questions related to NYC parking and tickets data.

The following 4 questions were answered using this code:

1. When are tickets most likely to be issued?
2. What are the most common years and types of cars to be ticketed?
3. Where are tickets most commonly issued?
4. Which color of the vehicle is most likely to get a ticket?

## Getting Started

Proceed to clone the repository into the Cloud cluster root folder (./).

`git clone https://github.com/rosamsierrap/Project1.git`


## Data

The data used in this analysis was obtained from the NYC Open Data website, which can be accessed here: https://data.cityofnewyork.us/City-Government/Parking-Violations-Issued-Fiscal-Year-2023/pvqr-7yc4

## Usage

To run this code you need a functional HDFS system running, for our experiments a 3 node cluster hosted on Google Cloud was the way to go. Two worker nodes and one manager orchestrating.
The driver code is stored in the file `part1.sh` and it will run the mappers/reducer to answer all the questions. Make sure to double check the appropiate location for the data csv, it can be found
inside of the driver code where there's a copyFromLocal statement `/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/nyc_parking_violations_data.csv /p1/input/`. 
This route is expected to be different depending on each system file distribution. 

## Findings

1. 9AM is the time at which more tickets are issued.
2. 2021 is the car year with more issued tickets, Suburban would be the vehicle type.
3. NY is the state at which more tickets are issued.
4. Gray vehicles seem to be the ones being issued more tickets.

## Conclusion 

Through the use of this MapReduce framework we are able to analyze NYC parking and tickets distributed data and answer some important questions about parking/driving violations. With this analysis, we can gain insights into which violations are most common or how the vehicles getting them look like.

