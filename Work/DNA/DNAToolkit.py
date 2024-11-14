# creating functions to handle DNA sequences

from sequences import *
from collections import Counter
import re

"""(string) Verify that string is DNA"""

def valid_seq(seq):
    DNA = seq.upper()
    for nuc in DNA:
        if nuc not in base_dict["DNA"]:
            return False
    return DNA


"""(list) Counts frequency of each Nucleotide"""


def nuc_freq(seq):
    nucDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        nucDict[nuc] += 1
    return list(nucDict.values())


"""(string) Adds the complement sequence of DNA to existing sequence"""


def comp(seq):
    # creates a map for replacing char's
    trans = seq.maketrans(dnacomp_dict)
    # replaces keys with values per maketrans()
    comp_DNA = seq.translate(trans)
    return comp_DNA


"""(string) Returns the reverse of a complement sequence"""


def rev_comp(seq):
    rev_comp = comp(seq)[::-1]
    return rev_comp


"""(string) Transcripts from DNA to RNA"""


def DNA_RNA(seq):
    return seq.replace("T", "U")


"""(list) Calculates 'G' and 'C' content in strand"""


def GC_count(seq):
    G_content = seq.count("G")
    C_content = seq.count("C")
    return f"{(G_content + C_content)/len(seq)*100}%"


"""(list) Returns G and C content of given range of a subsequence of DNA"""


def GC_count_subseq(seq, k=10):
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i : i + k]
        res.append(GC_count(subseq))
    return res


"""(dict) Returns dictionary with the type and count of aminoacids found in sequence"""


def aminoacid_count(seq):
    # amino_count = dict(Counter(trans_codons(seq)))
    amino_count = {}
    for i in trans_codons(seq):
        if i not in amino_count:
            amino_count[i] = 1
        else:
            amino_count[i] += 1
    return amino_count


"""(dict) Returns the frequency of codons for a given aminoacid in sequence"""


def amino_search(seq, aminoacid):
    codon_list = []
    freq = 0
    for i in range(0, len(seq) - 2, 3):
        subseq = seq[i : i + 3]
        if DNA[subseq] == aminoacid:
            freq += 1
            codon_list.append(subseq)
    codon_dict = dict(Counter(codon_list))
    for key, value in codon_dict.items():
        codon_dict[key] = f"{round((value/freq)*100, 2)}%"
    return codon_dict


"""(list) Returns translated codons from given sequence at a given starting position"""


def trans_codons(seq, init_pos=0):
    # for a codon (eg.'TAA') that is found as key in codontab dictionary, append its value to a list
    return [DNA[seq[i : i + 3]] for i in range(init_pos, len(seq) - 2, 3)]


"""(list) Uses the trans_codons function and returns a list (of strings) of translated open-reading frames (6) of given sequence"""


def gen_reading_frames(seq):
    frame_list = []
    frame_list.append("".join(trans_codons(seq)))
    frame_list.append("".join(trans_codons(seq, 1)))
    frame_list.append("".join(trans_codons(seq, 2)))
    frame_list.append("".join(trans_codons(rev_comp(seq))))
    frame_list.append("".join(trans_codons(rev_comp(seq), 1)))
    frame_list.append("".join(trans_codons(rev_comp(seq), 2)))
    return frame_list


"""(list) Uses re. module to find start, stop codons to generate a string of viable aminoacids as a ribosome would"""


def frame_to_protein(aa_seq):
    proteins = []
    pattern = r"(?=(M[A-Z]+\*))"
    matches = re.findall(pattern, aa_seq)
    for match in matches:
        proteins.append(match.replace("*", ""))
    return proteins

"""(tuple of list of tuples) Sorts all reading frames and their respective possible proteins in a list of tuples"""

def all_trans_rfs(aa_seq):
    protein_dict = {}
    for i, frame in enumerate(gen_reading_frames(aa_seq)):
        protein_dict[f"{i+1}. {frame}"] = (
            f">> Possible protein(s) found in frame ({i+1}):\n{frame_to_protein(frame)}"
        )
    return list(protein_dict.items())


# def frame_to_prot(aa_seq):
#    current_prot = []
#    proteins = []
#    for aa in aa_seq:
#        if aa == "*":
#            for p in current_prot:
#                proteins.append(p)
#            current_prot = []
#        elif aa == "M":
#            current_prot.append("")
#        for i in range(len(current_prot)):
#            current_prot[i] += aa
#    return proteins


# scan sequence of aminoacids
# if theres '*', 'M' in sequence, return the that starts with 'M' and ends with '*'
# eg. for - 'MTSSDPLLT*TDPSTL', return 'TSSDPLLT'
