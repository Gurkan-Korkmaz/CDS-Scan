import glob
import csv

with open('AnalyzedCDS.csv','w'):    # This part empties Analyzed.csv if it exists
    pass

with open('AnalyzedCDS.csv', 'w', newline='') as csvfile: #This will first write the complet header
    writer = csv.writer(csvfile)
    Name = ("provided by Gürkan Korkmaz", "http://orcid.org/0000-0003-1911-027X")
    header = ("Sequence", "TotalCDS", "Uncounted", "%Uncounted", "TGA", "TAG", "TAA", "%TGA", "%TAG", "%TAA", "CDSGC", "OffTGA", "OffTAG", "OffTAA", "%OffTGA", "%OffTAG", "%OffTAA", 'CDS Gs', 'CDS Cs', 'CDS As', 'CDS Ts', )
    writer.writerow(Name)
    writer.writerow(header)
#This will print out all files loaded in  the same directory
for filename in glob.glob('*.fna*'):
    print(filename)
#Total Number of Coding Sequences
    substringCDS = ">"
    Total = (open(filename, 'r').read().count(substringCDS))
#Canonical Stop Codons
    substringcanonicalTGA = "TGA\n>"
    TGA = (open(filename, 'r').read().count(substringcanonicalTGA))
    substringcanonicalTAG = "TAG\n>"
    TAG = (open(filename, 'r').read().count(substringcanonicalTAG))
    substringcanonicalTAA = "TAA\n>"
    TAA = (open(filename, 'r').read().count(substringcanonicalTAA))
    RatioTGA = 1 + TGA / (1 + TGA + TAG + TAA)
    RatioTAG = 1 + TAG / (1 + TGA + TAG + TAA)
    RatioTAA = 1 + TAA / (1 + TGA + TAG + TAA)
#Uncounted Stops
    Uncounted = Total - (TGA + TAG +TAA)
    RatioUncounted = Uncounted / Total
#GC content
    substringcanonicalCDSG = "G"
    CDSG = (open(filename, 'r').read().count(substringcanonicalCDSG))
    substringcanonicalCDSC = "C"
    CDSC = (open(filename, 'r').read().count(substringcanonicalCDSC))
    substringcanonicalCDSA = "A"
    CDSA = (open(filename, 'r').read().count(substringcanonicalCDSA))
    substringcanonicalCDST = "T"
    CDST = (open(filename, 'r').read().count(substringcanonicalCDST))
    GC = (CDSG+CDSC)/(CDSA+CDSC+CDSG+CDST)
#OffFrameTGA
    substringOffTGA1 = "TGA"
    OffTGA1 = (open(filename, 'r').read().count(substringOffTGA1))
    substringOffTGA2 = "TG\nA"
    OffTGA2 = (open(filename, 'r').read().count(substringOffTGA2))
    substringOffTGA3 = "T\nGA"
    OffTGA3 = (open(filename, 'r').read().count(substringOffTGA3))
    OffTGA = OffTGA1 + OffTGA2 + OffTGA3
#OffFrameTAG
    substringOffTAG1 = "TAG"
    OffTAG1 = (open(filename, 'r').read().count(substringOffTAG1))
    substringOffTAG2 = "TA\nG"
    OffTAG2 = (open(filename, 'r').read().count(substringOffTAG2))
    substringOffTAG3 = "T\nAG"
    OffTAG3 = (open(filename, 'r').read().count(substringOffTAG3))
    OffTAG = OffTAG1 + OffTAG2 + OffTAG3
#OffFrameTAA
    substringOffTAA1 = "TAA"
    OffTAA1 = (open(filename, 'r').read().count(substringOffTAA1))
    substringOffTAA2 = "TA\nA"
    OffTAA2 = (open(filename, 'r').read().count(substringOffTAA2))
    substringOffTAA3 = "T\nAA"
    OffTAA3 = (open(filename, 'r').read().count(substringOffTAA3))
    OffTAA = OffTAA1 + OffTAA2 + OffTAA3
#OffFrame Ratio
    OffRatioTGA = OffTGA / (OffTGA + OffTAG + OffTAA)
    OffRatioTAG = OffTAG / (OffTGA + OffTAG + OffTAA)
    OffRatioTAA = OffTAA / (OffTGA + OffTAG + OffTAA)

#Writes analysis into csv
    analyzed = (filename, Total, Uncounted, RatioUncounted, TGA, TAG, TAA, RatioTGA, RatioTAG, RatioTAA, GC, OffTGA, OffTAG, OffTAA, OffRatioTGA, OffRatioTAG, OffRatioTAA, CDSG, CDSC, CDSA, CDST)
#This will write a file named Analyzed.csv in write mode and wont add a newline between writerow's
    with open('AnalyzedCDS.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(analyzed)
