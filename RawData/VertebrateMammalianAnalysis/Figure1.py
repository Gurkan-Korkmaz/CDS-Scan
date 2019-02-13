from matplotlib import pyplot as plt
from matplotlib import style
import csv
import pylab
#style.use('ggplot') #Uses the style ggplot
Title = 'Vertebrate Mammalian - CDS Cognate Stops'
plt.title(Title)
plt.xlabel ('GC (%)')
plt.ylabel ('frequency')
#pylab.xlim([0.1,0.8])#Changes the range of the x axis
pylab.xlim([0,1])
pylab.ylim([0,0.7])
GC = []
TAG = []
TGA = []
TAA = []

with open ( 'AnalyzedAll.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        next(reader)
        for row in reader:
            temp=row[24]
            GC.append(temp)
            temp=row[8]
            TAG.append(temp)
            temp=row[7]
            TGA.append(temp)
            temp=row[9]
            TAA.append(temp)

plt.scatter(GC,TAG, label = 'TAG')
plt.scatter(GC,TGA, label = 'TGA')
plt.scatter(GC,TAA, label = 'TAA')
plt.legend(loc=2) #Various locations available
plt.savefig('VertebrateMammalianCDSCognateStopsFigure1.png', dpi=1000)
plt.show() #Otherwise it wont show the actual plot