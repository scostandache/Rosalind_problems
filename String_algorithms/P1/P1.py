
f=open('P1/rosalind_revc.txt','r')
DNA=f.read()
DNA=list(DNA)
DNA.reverse()
for i in range(len(DNA)):
    if DNA[i] == 'T':
        DNA[i]='A'
    elif DNA[i]=="A":
        DNA[i]='T'
    elif DNA[i]=='C':
        DNA[i]='G'
    elif DNA[i]=='G':
        DNA[i]='C'


DNA="".join(DNA)

f=open("P1/result.txt","w")

f.write(DNA)



