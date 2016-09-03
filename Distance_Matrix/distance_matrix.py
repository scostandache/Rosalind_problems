from useful_functions import fasta_reader
import numpy as np

def p_distance(dna_one, dna_two):
    differences=0.0
    for c1,c2 in zip(dna_one,dna_two):
        if c1!=c2:
            differences+=1
    return differences/len(dna_one)

dna_list=fasta_reader.get_whole_strings('dna_list.txt')

dna_size=len(dna_list)

dist_matrix=np.zeros((dna_size,dna_size),dtype=float)

for i in range(dna_size):
    for j in range(dna_size):
        dist_matrix[i][j]=p_distance(dna_list[i][1],dna_list[j][1])


for line in dist_matrix:
    print line