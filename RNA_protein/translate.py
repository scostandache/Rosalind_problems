table={}
f=open("codon","r")
for line in f:
    line=line.split(" ")
    table[line[0]]=line[1].strip("\n")
s="AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
x=[]
for i in range(0,len(s)-3,3):
    x.append(   table[s[i:i+3]])
print "".join([str(a)for a in x])

