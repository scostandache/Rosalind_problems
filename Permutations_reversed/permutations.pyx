import itertools
f=open("result","w")
cdef inline swap(int *a, int *b):
    cdef int aux
    aux=a[0]
    a[0]=b[0]
    b[0]=aux


cdef inline heap_alg(int n, int dim, int a[]):
    cdef int i
    if(n==1):

        f.write(" ".join(str(a[i]) for i in range(dim)))
        f.write("\n")
    else:
        for i in range(n-1):

            heap_alg(n-1,dim,a)
            if n %2==0:
                swap(&a[i],&a[n-1])
            else:
                swap(&a[0],&a[n-1])

        heap_alg(n-1,dim,a)

cdef int n=4
cdef int a[4]
a=[1,2,3,4]


def plusAndMinusPermutations(items):
    for p in itertools.permutations(items):
        for signs in itertools.product([-1,1], repeat=len(items)):
            f.write(" ".join([ str(a*sign) for a,sign in zip(p,signs)]))
            f.write("\n")

plusAndMinusPermutations(a)

print (2**4)*1*2*3*4
