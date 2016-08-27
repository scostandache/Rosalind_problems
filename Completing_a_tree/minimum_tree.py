import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

f=open("sample.txt","r")
no=int(f.readline())

adj_mat=np.full((no,no),1)
num=0
for pair in f.readlines():
    a,b= int(pair.split(" ")[0]), int(pair.split(" ")[1].strip("\n"))
    adj_mat[a-1][b-1]=2
    num+=1


print adj_mat
X=csr_matrix(adj_mat)


Tcsr=minimum_spanning_tree(X)
#Tcsr.toarray().astype(int)
i=0
for line in Tcsr:
    i+=1

print i-num-1