f=open("rosalind_hamm.txt","r")
s,t=f.readlines()
dist=0
for i in range(len(s)):
    if(s[i]!=t[i]):
        dist+=1
print len(s)
print dist