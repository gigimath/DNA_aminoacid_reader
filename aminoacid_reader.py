#!/usr/bin/env python
# coding: utf-8

# In[86]:


import os

print('This program take in input a DNA sequence and calculate the numbers of codond inside, \nshowing them in a decreasing order.')
print('The output will be displeyed here and also write in a file inside the output folder\n')


import argparse

my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'
my_parser.add_argument('-f','--fileName',type=str, nargs='?',default='dna_string_example.txt', action='store',help='type dataset name')

args = my_parser.parse_args()
name_file = args.fileName

path_this_dir = os.getcwd()

file = open(path_this_dir+os.sep+'input'+os.sep+name_file, "r")
dna = file.read()


dict_dna = {'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
 'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
 'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
 'Lys': ['AAA', 'AAG'],
 'Asn': ['AAT', 'AAC'],
 'Met': ['ATG'],
 'Asp': ['GAT', 'GAC'],
 'Phe': ['TTT', 'TTC'],
 'Cys': ['TGT', 'TGC'],
 'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
 'Gln': ['CAA', 'CAG'],
 'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
 'Glu': ['GAA', 'GAG'],
 'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
 'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
 'Trp': ['TGG'],
 'His': ['CAT', 'CAC'],
 'Tyr': ['TAT', 'TAC'],
 'Ile': ['ATT', 'ATC', 'ATA'],
 'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
 'stop': ['TAG', 'TGA', 'TAA']}

dict_triple2aminoacid = {}
for k, v in dict_dna.items():
    for triple in v:
        dict_triple2aminoacid[triple] = k


# In[71]:


n = 3
dna_split = [dna[i:i+n] for i in range(0, len(dna), n)]


# In[88]:


dict_aminoacid_count = {k:0 for k in dict_dna.keys()}

flag = False
for triple in dna_split:
    if len(triple) == 3:
        try:
            aminoacid = dict_triple2aminoacid[triple]
            dict_aminoacid_count[aminoacid] +=1
        except:
            flag = True
            print('There is a character not allowed in DNA sequance')
            print('Review the DNA sequance and play this program again')
            print('The only characters allowed are A,C,G,T')

list_decrease = sorted(dict_aminoacid_count.items(), key=lambda item: item[1])[::-1]
dict_aminoacid_count_sorted = {k:v for k, v in list_decrease}



if not flag:
    name_out_file = path_this_dir+os.sep+'output'+os.sep+name_file+'_processed'+'.txt'
    log_file = open(name_out_file,"w")
    
    for k,v in dict_aminoacid_count_sorted.items():
        if k != 'stop':
            print('Aminoacid:',k,', count:',v)
            print('Aminoacid:',k,', count:',v, file = log_file)
        
    print('\nNumbers of stops codons:', dict_aminoacid_count_sorted['stop'])
    print('\nNumbers of stops codons:', dict_aminoacid_count_sorted['stop'], file = log_file)
    
    log_file.close()






