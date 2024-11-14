from sequences import *
from collections import Counter
from readwrite import *
import re



class bio_seq:

    def __init__(self, seq="ACTG", seq_type="DNA", label="No label given"):
        self.seq = seq.upper()
        self.seq_type = seq_type
        self.label = label
        self.is_valid = self.__validate()
        assert self.is_valid, f"Data is not a valid {self.seq_type} sequence"

    def __validate(self):
        return set(base_dict[self.seq_type]).issuperset(self.seq)

    def randomseq(self, n, seq_type="DNA"):
        seq = "".join([random.choice(base_dict[seq_type]) for _ in range(n)])
        # re-initilize the class to match generated sequence
        self.__init__(seq, seq_type, "Randomly generated sequence")

    def transcription(self):
        if self.seq_type == "DNA":
            return f"[RNA]: {self.seq.replace('T', 'U')}"
        return "Not a DNA sequence"

    def rev_comp(self):
        if self.seq_type == "DNA":
            trans = self.seq.maketrans(dnacomp_dict)
        elif self.seq_type == "RNA":
            trans = self.seq.maketrans(rnacomp_dict)
        return self.seq.translate(trans)[::-1]


    def GC_count_subseq(self, k=10):
        res = []
        for i in range(0, len(self.seq) - k + 1, k):
            subseq = self.seq[i : i + k]
            res.append(f"{round((subseq.count('G') + subseq.count('C'))/len(subseq)*100)}%")
        return res

    def trans_codons(self, init_pos=0):
        # for a codon (eg.'TAA') that is found as key in codontab dictionary, append its value to a list
        if self.seq_type == "DNA":
            return [DNA[self.seq[i : i + 3]] for i in range(init_pos, len(self.seq) - 2, 3)]
        elif self.seq_type == "RNA":
            return [RNA[self.seq[i : i + 3]] for i in range(init_pos, len(self.seq) - 2, 3)]

    def amino_search(self, aminoacid):
        codon_list = []
        freq = 0
        if self.seq_type == "DNA":
            for i in range(0, len(self.seq) - 2, 3):
                subseq = self.seq[i : i + 3]
                if DNA[subseq] == aminoacid:
                    freq += 1
                    codon_list.append(subseq)
        if self.seq_type == "RNA":
            for i in range(0, len(self.seq) - 2, 3):
                subseq = self.seq[i : i + 3]
                if RNA[subseq] == aminoacid:
                    freq += 1
                    codon_list.append(subseq)

        codon_dict = dict(Counter(codon_list))
        for key, value in codon_dict.items():
            codon_dict[key] = f"{round((value/freq)*100, 2)}%"
        return codon_dict

    def gen_reading_frames(self):
        frame_list = []
        frame_list.append("".join(self.trans_codons(0)))
        frame_list.append("".join(self.trans_codons(1)))
        frame_list.append("".join(self.trans_codons(2)))
        tmp_seq = bio_seq(self.rev_comp(), self.seq_type)
        frame_list.append("".join(tmp_seq.trans_codons(0)))
        frame_list.append("".join(tmp_seq.trans_codons(1)))
        frame_list.append("".join(tmp_seq.trans_codons(2)))
        del tmp_seq
        return frame_list

    def frame_to_protein(self, aa_seq):
        proteins = []
        pattern = r"(?=(M[A-Z]+\*))"
        matches = re.findall(pattern, aa_seq)
        for match in matches:
            proteins.append(match.replace("*", ""))
        return proteins

    def all_trans_rfs(self):
        protein_dict = {}
        for i, frame in enumerate(self.gen_reading_frames()):
            protein_dict[f"{i+1}. {frame}"] = (
                f">> Possible protein(s) found in frame ({i+1}): {self.frame_to_protein(frame)}"
            )
        return list(protein_dict.items())



    @property
    def GC_count(self):
        G_content = self.seq.count("G")
        C_content = self.seq.count("C")
        return f"{round((G_content + C_content)/len(self.seq)*100)}%"

    @property
    def nuc_frequency(self):
        return dict(Counter(self.seq))

    @property
    def show_info(self):
        return (
            f"\n[Label]: {self.label}\n[Sequence]: {self.seq}\n[Type]: {self.seq_type}\n[Length]: {len(self.seq)}"
        )


#DNA_1 = bio_seq ()
#DNA_1.randomseq(1000)
#print(DNA_1.show_info)
#print(DNA_1.rev_comp())
#print(DNA_1.transcription())
#print(DNA_1.nuc_frequency)
#print(DNA_1.GC_count_subseq())
#print(DNA_1.GC_count)
#print(DNA_1.trans_codons(0))
#print(DNA_1.amino_search("M"))
#print(DNA_1.gen_reading_frames())
#for key, values in DNA_1.all_trans_rfs():
#    print(f"\n{key}\n\n{values}\n")



#writefile("test.txt", f"{DNA_1.show_info}\n", "a")
#for i, p in (DNA_1.all_trans_rfs()):
#        f = writefile("test.txt", f"{i}\n {p}\n", "a")



