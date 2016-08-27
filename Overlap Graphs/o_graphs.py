from useful_functions.fasta_reader import *

def find_graph(strings_file,k):
    pref_list=get_prefixes(strings_file,k)
    suff_list=get_suffixes(strings_file,k)

    for pref in pref_list:

        for suff in suff_list:
            if(pref[0]!=suff[0]):
                if(pref[1]==suff[1]):

                    print suff[0].strip(">"),pref[0].strip(">")


find_graph("sample.txt",3)
