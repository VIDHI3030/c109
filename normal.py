import csv
import plotly.express as px
import plotly.figure_factory as ff 
import pandas as pd 
import statistics

dataFile=pd.read_csv("csv/normal.csv")
height=dataFile["Height"].to_list()
weight=dataFile["Weight"].to_list()
Hmean=statistics.mean(height)
Wmean=statistics.mean(weight)
Hmode=statistics.mode(height)
Wmode=statistics.mode(weight)
Hmedian=statistics.median(height)
Wmedian=statistics.median(weight)
Hstd=statistics.stdev(height)
Wstd=statistics.stdev(weight)
hstdev1start,hstdev1end=Hmean-Hstd,Hmean+Hstd
hstdev2start,hstdev2end=Hmean-2*Hstd,Hmean+2*Hstd
hstdev3start,hstdev3end=Hmean-3*Hstd,Hmean+3*Hstd
wstdev1start,wstdev1end=Wmean-Wstd,Wmean+Wstd
wstdev2start,wstdev2end=Wmean-2*Wstd,Wmean+2*Wstd
wstdev3start,wstdev3end=Wmean-3*Wstd,Wmean+3*Wstd
Heightwithinstdev1=[r for r in height if r>hstdev1start and r<hstdev1end]
Heightwithinstdev2=[r for r in height if r>hstdev2start and r<hstdev2end]
Heightwithinstdev3=[r for r in height if r>hstdev3start and r<hstdev2end]

Weightwithinstdev1=[r for r in weight if r>wstdev1start and r<wstdev1end]
Weightwithinstdev2=[r for r in weight if r>wstdev2start and r<wstdev2end]
Weightwithinstdev3=[r for r in weight if r>wstdev3start and r<wstdev2end]
print("height data within first stdev ",len(Heightwithinstdev1)*100/len(height))
print("height data within second stdev ",len(Heightwithinstdev2)*100/len(height))
print("height data within third stdev ",len(Heightwithinstdev3)*100/len(height))

print("weight data within first stdev ",len(Weightwithinstdev1)*100/len(weight))
print("weight data within second stdev ",len(Weightwithinstdev2)*100/len(weight))
print("weight data within third stdev ",len(Weightwithinstdev3)*100/len(weight))
