

from itertools import permutations


def cyclo_peptide_sequencing(masses):
  AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
  
  masses.sort()

  MassToAminoAcid = {57: ['G'], 71: ['A'], 87: ['S'], 97: ['P'], 99: ['V'], 101: ['T'], 103: ['C'],
    113: ['I', 'L'], 114: ['N'], 115: ['D'], 128: ['K', 'Q'], 129: ['E'], 131: ['M'], 137: ['H'],
    147: ['F'], 156: ['R'], 163: ['Y'], 186: ['W']}

  criteria = masses[-1]
  sequenced = []

  # Find all amino acids whose masses occur in Spectrum. Add to List.
  aminoAcids = []

  for mass in masses:
    if MassToAminoAcid.get(mass):
      for m in MassToAminoAcid[mass]:
        # if m not in aminoAcids:
        aminoAcids.append(m)
  
  # Extend each peptide in List by each of 18 different amino acid masses
  peptides = [[i] for i in range(len(aminoAcids))]

  while peptides:
    # print(peptides)
    newPeptides = []
    for i in range(len(aminoAcids)) :
        for peptide in peptides:
          if i not in peptide:
            newPeptides.append([i] + peptide)
            newPeptides.append(peptide + [i])

    peptides = newPeptides

    # Trim inconsistent peptides from List
    newPeptides = []
    for peptide in peptides:
      mass = 0
      for aminoAcid in peptide:
        mass += AminoAcidMass[aminoAcids[aminoAcid]]
      
      if mass in masses:
        newPeptides.append(peptide)

      if mass == criteria and peptide not in sequenced:
        sequenced.append(peptide)
    
    peptides = newPeptides
    # print(peptides)

  return sequenced

name = "input2.txt"
# name = "Tyrocidine_B1_theoretical_spectrum.txt"
f = open(f"./data/{name}", 'r')
string = f.readline().strip()
masses = list(map(int, string.split(' ')))
# cyclo_peptide_sequencing(masses)
print(*cyclo_peptide_sequencing(masses), sep="\n")