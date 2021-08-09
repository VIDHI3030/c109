import csv
import plotly.express as px
import plotly.figure_factory as ff 
import pandas as pd 
import statistics

dataFile=pd.read_csv("csv/StudentsPerfomance.csv")
math score=dataFile["math score"].to_list()
reading score=dataFile["reading score"].to_list()
Mmean=statistics.mean(math score)
Rmean=statistics.mean(reading score)
Mmode=statistics.mode(math score)
Rmode=statistics.mode(reading score)
Mmedian=statistics.median(math score)
Rmedian=statistics.median(reading score)
Mstd=statistics.stdev(math score)
Wstd=statistics.stdev(reading score)
mstdev1start,mstdev1end=Mmean-Mstd,Mmean+Mstd
hstdev2start,hstdev2end=Mmean-2*Hstd,Mmean+2*Hstd
mstdev3start,mstdev3end=Mmean-3*Hstd,Mmean+3*Hstd
rstdev1start,rstddev1end=Rmean-Rstd,Rmean+Wstd
rstdev2start,rstddev2end=Rmean-2*Rstd,Rmean+2*Wstd
rstdev3start,rstdev3end=Rmean-3*Rstd,Rmean+3*Wstd
Heightwithinstdev1=[r for r in math score if r>mstdev1start and r<mstdev1end]
Heightwithinstdev2=[r for r in math score if r>mstdev2start and r<mstdev2end]
Heightwithinstdev3=[r for r in math score if r>mstdev3start and r<mstdev2end]

Weightwithinstdev1=[r for r in reading score if r>rstdev1start and r<rstdev1end]
Weightwithinstdev2=[r for r in reading score if r>rstdev2start and r<rstdev2end]
Weightwithinstdev3=[r for r in reading score if r>rstdev3start and r<rstdev2end]
print("math score data within first stdev ",len(Heightwithinstdev1)*100/len(math score))
print("math score data within second stdev ",len(Heightwithinstdev2)*100/len(math score))
print("math score data within third stdev ",len(Heightwithinstdev3)*100/len(math score))

print("reading score data within first stdev ",len(Weightwithinstdev1)*100/len(reading score))
print("reading score data within second stdev ",len(Weightwithinstdev2)*100/len(reading score))
print("reading score data within third stdev ",len(Weightwithinstdev3)*100/len(reading score))
