
f=open('sets.txt','r')
results=open('result.txt','w')
n=f.readline()

raw_a=f.readline().strip('\n{}')
a=set(raw_a.split(', '))


raw_b=f.readline().strip('\n{}')
b=set(raw_b.split(', '))

full_set={ str(i) for i in range(1,int(n)+1)}


reunion= [int(el) for el in a|b]
reunion= str(reunion).replace('[','{').replace(']','}')

intersection= [int(el) for el in a&b]
intersection= str(intersection).replace('[','{').replace(']','}')

a_b=[int(el) for el in a-b]
a_b= str(a_b).replace('[','{').replace(']','}')

b_a=[int(el) for el in b-a]
b_a= str(b_a).replace('[','{').replace(']','}')


a_complement=[int(el) for el in (full_set-a)]
a_complement= str(a_complement).replace('[','{').replace(']','}')



b_complement=[int(el) for el in (full_set-b)]
b_complement= str(b_complement).replace('[','{').replace(']','}')

results.write(reunion+'\n')
results.write(intersection+'\n')
results.write(a_b+'\n')
results.write(b_a+'\n')
results.write(a_complement+'\n')
results.write(b_complement+'\n')




