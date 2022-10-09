aa_table_dna = {'K': ['AAA', 'AAG'], 'N': ['AAC', 'AAT'], 'T': ['ACA', 'ACC', 'ACG', 'ACT'], 'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGT'], 'S': ['AGC', 'AGT', 'TCA', 'TCC', 'TCG', 'TCT'], 'I': ['ATA', 'ATC', 'ATT'], 'M': ['ATG'], 'Q': ['CAA', 'CAG'], 'H': ['CAC', 'CAT'], 'P': ['CCA', 'CCC', 'CCG', 'CCT'], 'L': ['CTA', 'CTC', 'CTG', 'CTT', 'TTA', 'TTG'], 'E': ['GAA', 'GAG'], 'D': ['GAC', 'GAT'], 'A': ['GCA', 'GCC', 'GCG', 'GCT'], 'G': ['GGA', 'GGC', 'GGG', 'GGT'], 'V': ['GTA', 'GTC', 'GTG', 'GTT'], '*': ['TAA', 'TAG', 'TGA'], 'Y': ['TAC', 'TAT'], 'C': ['TGC', 'TGT'], 'W': ['TGG'], 'F': ['TTC', 'TTT']}


def complement(c):
  nucleotide_complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

  return nucleotide_complement[c]

def peptide_encoding(strand, peptide):
  dnas = {}
  codons = []
  anss = []

  for p in peptide:
    codons.append(aa_table_dna[p])

  def rec(i, ans):
    if i == len(peptide):
      dnas[ans] = 1
      ans = list(ans)
      ans.reverse()
      dnas["".join(list(map(complement, ans)))] = 1
      return 
    
    for codon in codons[i]:
      rec(i+1, ans+codon)
  
  rec(0, "")
  
  k = len(peptide) * 3

  for i in range(len(strand) - k + 1):
    window = strand[i:i+k]
    if dnas.get(window):
      anss.append(window)
  
  return anss


# name = input()
# f = open(f"./data/{name}", "r")
# strand = f.readline().strip()
# peptide = f.readline().strip()
# anss = peptide_encoding(strand, peptide)
# print("\n".join(anss))

name = input()
f = open(f"./data/{name}", "r")
strand = f.read().strip()
strand = strand.split('\n')
strand = "".join(strand)
# print(strand)
peptide = "VKLFPWFNQY"
anss = peptide_encoding(strand, peptide)
f.close()

fo = open(f"./data/Bacillus_brevis_output.txt", "w")
fo.write("\n".join(anss))
fo.close()