def get_whole_strings(file_name):
    f=open(file_name,"r")
    strings=f.readlines()
    indexes=[]
    DNA_pairs=[]

    for i in range(0, len(strings)):
        if ">" in strings[i]:
            indexes.append(i)
            #DNA_pairs.append( (strings[i].strip('\n>'),strings[i+1].strip('\n')))

    for i in range(len(indexes)-1):

        idx1=indexes[i]
        idx2=indexes[i+1]
        fasta=""
        for j in range(idx1+1,idx2):
            fasta+=strings[j].strip("\n")

        pair=(strings[idx1].strip("\n"),fasta)
        DNA_pairs.append(pair)
    fasta=""
    for i in range(indexes[len(indexes)-1]+1, len(strings)):
        fasta += strings[i].strip("\n")
    DNA_pairs.append((strings[indexes[len(indexes)-1]].strip("\n"), fasta))
    return DNA_pairs

def get_prefixes(file_name,k):
    f = open(file_name, "r")
    strings = f.readlines()
    indexes = []
    DNA_pairs = []

    for i in range(0, len(strings)):
        if ">" in strings[i]:
            indexes.append(i)
            # DNA_pairs.append( (strings[i].strip('\n>'),strings[i+1].strip('\n')))

    for i in range(len(indexes) - 1):

        idx1 = indexes[i]
        idx2 = indexes[i + 1]
        fasta = ""
        for j in range(idx1 + 1, idx2):
            fasta += strings[j].strip("\n")

        pair = (strings[idx1].strip("\n"), fasta[0:k])
        DNA_pairs.append(pair)
    fasta = ""

    for i in range(indexes[len(indexes)-1]+1, len(strings)):
        fasta += strings[i].strip("\n")
    DNA_pairs.append((strings[indexes[len(indexes)-1]].strip("\n"), fasta[0:k]))
    return DNA_pairs

def get_suffixes(file_name,k):
    f = open(file_name, "r")
    strings = f.readlines()
    indexes = []
    DNA_pairs = []

    for i in range(0, len(strings)):
        if ">" in strings[i]:
            indexes.append(i)
            # DNA_pairs.append( (strings[i].strip('\n>'),strings[i+1].strip('\n')))

    for i in range(len(indexes) - 1):

        idx1 = indexes[i]
        idx2 = indexes[i + 1]
        fasta = ""
        for j in range(idx1 + 1, idx2):
            fasta += strings[j].strip("\n")

        pair = ( strings[idx1].strip("\n") , fasta[-k:])
        DNA_pairs.append(pair)
    fasta = ""
    for i in range(indexes[len(indexes)-1]+1, len(strings)):
        fasta += strings[i].strip("\n")
    DNA_pairs.append( (strings[indexes[len(indexes)-1]].strip("\n"), fasta[-k:]) )

    return DNA_pairs

