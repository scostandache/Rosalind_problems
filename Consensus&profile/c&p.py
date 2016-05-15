f=open("rosalind_cons.txt","r")
strings=f.readlines()
str_list=[]
def find_column_max(c,m):
    max=m[0][c]
    poz=0
    for i in range (len(m)):
        if m[i][c]>max:
            max=m[i][c]
            poz=i
    return poz


for i in range(0,len(strings),2):
    str_list.append(strings[i+1].strip('\n>'))
profile=[]
for i in range(4):
    line=len(str_list[0])*[0]
    profile.append(line)

for i in range(len(str_list[0])):
    for el in str_list:
        if el[i]=='A':
            profile[0][i]+=1
        elif el[i]=='C':
            profile[1][i]+=1
        elif el[i]=='G':
            profile[2][i]+=1
        elif el[i]=='T':
            profile[3][i]+=1

max_positions=[]
for i in range(len(profile[0])):
    max_positions.append(find_column_max(i,profile))
output=""
for a in max_positions:
    if a==0:
        output+='A'
    elif a==1:
        output+='C'
    elif a==2:
        output+='G'
    elif a==3:
        output+='T'

print output
print "A: "," ".join(str(x) for x in profile[0])
print "C: "," ".join(str(x) for x in profile[1])
print "G: "," ".join(str(x) for x in profile[2])
print "T: "," ".join(str(x) for x in profile[3])