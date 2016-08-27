import numpy as np

f=open("sample.txt","r")
no=int(f.readline())

adj_mat=np.eye(no,dtype=int)

for pair in f.readlines():
    a,b= int(pair.split(" ")[0]), int(pair.split(" ")[1].strip("\n"))
    adj_mat[a-1][b-1]=adj_mat[b-1][a-1]=1
num=0
for i in range(no):
    for j in range(no):
        if (adj_mat[i][j]==adj_mat[j][i]==1 and i!=j):
            num+=1
print no-num/2



