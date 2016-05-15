codon_table={}
f=open("codon","r")
for line in f:
    line=line.split(" ")
    codon_table[line[0]]=line[1].strip("\n")

def freqs():
    frequencies={}
    for a,b in codon_table.iteritems():
        if b not in frequencies:
            frequencies[b]=0
        frequencies[b]+=1
    return frequencies

def possibilities(s):
    f=freqs()
    n=f['Stop']
    for c in s:
        n*=f[c]
    return n

s=open("dataset","r").read().strip()

print possibilities(s)%1000000

