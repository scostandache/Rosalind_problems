from operator import itemgetter

def cg_content(dna):
    cg=0.0
    dna_list=list(dna)
    for s in dna_list:
        if s=='C' or s=='G':
            cg+=1.0

    percentage=round((100.0*cg)/len(dna_list),7)
    return percentage

f=open("rosalind_gc.txt","r")
pairs=f.readlines()
tuples_list=[]
for i in range(0,len(pairs),2):
    tuples_list.append(tuple([pairs[i].strip('\n>'),cg_content(pairs[i+1].strip('\n'))]))

sorted(tuples_list,key=itemgetter(1))

print tuples_list