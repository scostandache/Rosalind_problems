def get_strings(file_name):
    f=open(file_name,"r")
    strings=f.readlines
    DNA_pairs=[]
    for i in range(0, len(strings),2):
        DNA_pairs.append( (strings[i].strip('\n>'),strings[i+1]))

    return DNA_pairs

