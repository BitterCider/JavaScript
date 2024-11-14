#Testing the functions for handling DNA sequences

from sequences import *
from DNAToolkit import *
import random

def randomDNA(n):
        rndDNAstr = ''.join([random.choice(base_dict["DNA"])
                     for _ in range(int(n))])
        return rndDNAstr
#
#print(randomDNA(10))
#
print(f"\nFrequency of Nucleotides (A, C, G, T): {nuc_freq(rndDNAstr)}\n")
#print(f"5' {rndDNAstr} 3'")
#print(f"   {'|'*(len(rndDNAstr))}")
#print(f"3' {comp(rndDNAstr)} 5' [Complement]\n")
#print(f"5' {rev_comp(rndDNAstr)} 3' [Rev. Complement]\n")
#print(f"RNA: {DNA_RNA(rndDNAstr)}\n")
#print(f"Frequency of G and C in 'k' number of Nucleotide subsequences: {GC_count_subseq(rndDNAstr, k=10)}\n")
#print(f"G and C total percentage in strand: {GC_count(rndDNAstr)}\n")
#print(f"Type and count of aminoacids: {aminoacid_count(rndDNAstr)}\n")
#print(f"Frequency of given aminoacid as codon in original sequence: {amino_search(rndDNAstr, 'L')}\n")
#
#for key, values in all_trans_rfs(rndDNAstr):
#        print(f"{key}\n\n{values}\n")

print(len(rndDNAstr))