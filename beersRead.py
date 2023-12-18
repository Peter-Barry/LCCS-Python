import csv
import statistics as st
#import matplotlib.pyplot as plt
import plotly.express as plt
import pandas as pd
print("done")
data = pd.read_csv("beers.csv")
print("Read")
file = open("beers.csv", "r")
allData = list(csv.reader(file))
file.close()
print("CSv opened")
colName = allData[0]
print(colName)
sft = [int(row[3]) for row in allData[1:]]


