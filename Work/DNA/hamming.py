dna_str1 = "TTCGATCCATTG"
dna_str2 = "ATCAATCGATCG"

d = 0

for i in range(len(dna_str1)):
    if dna_str1[i] != dna_str2[i]:
        d += 1
print(f"Hamming Distance: {d}")
    
    
    
zipped_dna = zip(dna_str1, dna_str2)
dna_list = [(x, y) for x, y in zipped_dna if x != y]
print(len(dna_list))