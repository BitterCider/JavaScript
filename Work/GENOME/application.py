from Genome_TK import GenomeToolkit


sequence = "AATAAAGTTAAGAAAGCGT"
kmer = "AAAG"

gt = GenomeToolkit(sequence)

print(gt.k_mers(kmer))