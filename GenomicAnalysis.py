import glob
import csv
#This part empties Analyzed.csv if it exists
with open('AnalyzedGenomic.csv','w'):
    pass
#This will first write the complete header
with open('AnalyzedGenomic.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    Name = ("provided by Gürkan Korkmaz", "http://orcid.org/0000-0003-1911-027X")
    header = ("Sequence", "TotalCDS", "GenomicGC", 'GenomicOffTAG', 'GenomicOffTGA', 'GenomicOffTAA', 'Genomic Gs', 'Genomic Cs', 'Genomic As', 'Genomic Ts' )
    writer.writerow(Name)
    writer.writerow(header)
#This will print out all files loaded in  the same directory
for filename in glob.glob('*.fna*'):
    print(filename)
#Total Number of Coding Sequences
    substringCDS = ">"
    Total = (open(filename, 'r').read().count(substringCDS))
#GC content
    substringGenomicGCG = "G"
    GCG = (open(filename, 'r').read().count(substringGenomicGCG))
    substringGenomicGCC = "C"
    GCC = (open(filename, 'r').read().count(substringGenomicGCC))
    substringGenomicGCA = "A"
    GCA = (open(filename, 'r').read().count(substringGenomicGCA))
    substringGenomicGCT = "T"
    GCT = (open(filename, 'r').read().count(substringGenomicGCT))
    GC = (GCG+GCC)/(GCA+GCC+GCG+GCT)
    substringGenomicoffTAG = "TAG"
    TAG = (open(filename, 'r').read().count(substringGenomicoffTAG))
    substringGenomicoffTGA = "TGA"
    TGA = (open(filename, 'r').read().count(substringGenomicoffTGA))
    substringGenomicoffTAA = "TAA"
    TAA = (open(filename, 'r').read().count(substringGenomicoffTAA))
#Writes analysis into csv
    analyzedGC = (filename, Total, GC, TAG, TGA, TAA, GCG, GCC, GCA, GCT)
#This will write a file named Analyzed.csv in write mode and wont add a newline between writerow's
    with open('AnalyzedGenomic.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(analyzedGC)
