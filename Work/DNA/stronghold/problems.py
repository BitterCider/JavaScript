from sequences import *

# Count Nucleotides

def nuc_freq(seq):
    nucDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        nucDict[nuc] += 1
    return list(nucDict.values())


# DNA to RNA
def DNA_RNA(seq):
    return seq.replace("T", "U")

# DNA complement strand
def rev_comp(seq):
    trans = seq.maketrans(Nuc_Dict)
    seq = seq.translate(trans)[::-1]
    return (seq)

def GC_count(seq):
    G_content = seq.count("G")
    C_content = seq.count("C")
    return f"{(G_content + C_content)/len(seq)*100}%"

