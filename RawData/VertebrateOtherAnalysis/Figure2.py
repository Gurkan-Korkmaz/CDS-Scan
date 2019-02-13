from matplotlib import pyplot as plt
from matplotlib import style
import csv
import pylab
#style.use('ggplot') #Uses the style ggplot
Title = 'Vertebrate Other - CDS Off Stops'
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
            temp=row[15]
            TAG.append(temp)
            temp=row[14]
            TGA.append(temp)
            temp=row[16]
            TAA.append(temp)

plt.scatter(GC,TGA, label = 'TGA', color = 'Orange')
plt.scatter(GC,TAA, label = 'TAA', color = 'Green')
plt.scatter(GC,TAG, label = 'TAG', color = 'Blue')
plt.legend(loc=2) #Various locations available
plt.savefig('VertebrateOtherCDSOffStopsFigure2B.png', dpi=1000)
plt.show() #Otherwise it wont show the actual plot