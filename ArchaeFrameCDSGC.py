from matplotlib import pyplot as plt
from matplotlib import style
import csv
import pylab
#style.use('ggplot') #Uses the style ggplot
Title = 'Archaea'
plt.title(Title)
plt.xlabel ('CDS GC (%)')
plt.ylabel ('frequency')

genomicGC = []
TAG = []
TGA = []
TAA = []
offTAG = []
offTGA = []
offTAA = []
CDSGC = []

with open ( 'Archaea.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        next(reader)
        for row in reader:
            temp=row[19]
            genomicGC.append(temp)
            temp=row[10]
            CDSGC.append(temp)
            temp=row[8]
            TAG.append(temp)
            temp=row[7]
            TGA.append(temp)
            temp=row[9]
            TAA.append(temp)
            temp=row[15]
            offTAG.append(temp)
            temp=row[14]
            offTGA.append(temp)
            temp=row[16]
            offTAA.append(temp)


plt.scatter(CDSGC,TAG, label = 'TAG')
plt.scatter(CDSGC,TGA, label = 'TGA')
plt.scatter(CDSGC,TAA, label = 'TAA')
plt.legend(loc=1) #Various locations available
plt.show() #Otherwise it wont show the actual plot

