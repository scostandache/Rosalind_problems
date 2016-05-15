
f=open("result","w")
cdef inline swap(int *a, int *b):
    cdef int aux
    aux=a[0]
    a[0]=b[0]
    b[0]=aux


cdef inline heap_alg(int n, int dim, int a[]):

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

cdef int n=10
cdef int a[10]
a=[1,2,3,4,5,-1,-2,-3,-4,-5]

heap_alg(n,n,a)




