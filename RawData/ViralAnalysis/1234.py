#Example of how the scatter plots are created as shown in Figure 1 of the article.
#Example Dataset is Virus. (Figure 1G) Files are imported as .csv files.
#All Sub Figures in Figure 1 can be recreated by simply changing the input file name in line 23.
#Don't forget to adjust the Title (line 12) and (line 43) according to your input files (line 23).
#Note that the files in the repository are not in .csv format but can be exported easily into .csv file format.

from matplotlib import pyplot as plt
from matplotlib import style
import csv
import pylab
#style.use('ggplot') #Uses the style ggplot, in case you like the scatter plots from the programming language R
Title = 'Virus - CDS Cognate Stops' #Title shown above the scatter plot.
plt.title(Title)
plt.xlabel ('GC (%)')
plt.ylabel ('frequency')
#pylab.xlim([0.1,0.8]) #Changes the range of the x axis
pylab.xlim([0,1]) #Range of x axis
pylab.ylim([0,1]) #Range of y axis
GC = []
TAG = []
TGA = []
TAA = []

with open ( 'RawDataVirus.csv', 'r') as csvfile: #Open Database
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
plt.savefig('VirusCDSCognateStopsFigure1.png', dpi=1000) #Saves the scatter plot with a resolution of 1000 DPI
plt.show() #Otherwise it wont show the actual plot after running the script succesfully

#Publication Link will be added once available