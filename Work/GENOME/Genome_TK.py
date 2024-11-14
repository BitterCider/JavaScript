class GenomeToolkit:
    def __init__(self, seq):
        self.seq = seq  
              
    def k_mers(self, kmer):
        count = 0
        for i in range(len(self.seq)):
            if self.seq[i:i+len(kmer)] == kmer:
                count +=1
        return count