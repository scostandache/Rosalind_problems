import itertools

f=open("result","w")
alpha=list([ 'T', 'D', 'H', 'Y', 'K', 'L', 'N', 'B', 'V', 'F', 'S', 'A' ])

res=[]

for i in range(1,4):
    for b in itertools.product(alpha,repeat=i):
        res.append( ("".join(b) ).strip('')  )

def lex_ordered(c1,c2,a):
    n1=len(c1)
    n2=len(c2)
    if(n1<n2):
        if c1==c2[0:n1]:
            return True
    elif(n2<n1):
        if c2==c1[0:n2]:
            return False
    i=0
    while( i< n1 if n1<n2 else n2):
        if(c1[0:i]==c2[0:i]):
            i+=1
        else:

            break
    return True if a.index(c1[i-1])<a.index(c2[i-1]) else False


"""for i in range(len(res)-1):
    for j in range(0,len(res)-i-1):
        if(lex_ordered( res[j],res[j+1],alpha)==False):
            res[j],res[j+1]=res[j+1],res[j]"""



def qs(arr,low,high):

    if( low < high ):

        pivot=partition(arr,low,high)
        qs(arr,low,pivot)
        qs(arr,pivot+1,high)

def partition(arr,low,high):

    pivot = arr[low]
    left=low

    for i in range(low+1,high):
        if (  lex_ordered(arr[i], pivot,alpha )==False):

            left = left+1
            arr[i],arr[left]=arr[left],arr[i]

    arr[low], arr[left]=arr[left],arr[low]
    return left

qs(res,0,len(res))

res=reversed(res)

for line in res:
    f.write(line+"\n")
