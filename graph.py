import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
population = []
names = []

with open("pacensus.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    next(reader, None)
    for row in reader:
        population.append(int(row[30]))
        names.append(row[2].replace("County, Pennsylvania", ""))

plt.bar(names, population)
# plt.axis([0, 70, 0, 1750000])
plt.xticks(rotation=85)
plt.xlabel('Counties')
plt.ylabel('Population')
plt.show()
