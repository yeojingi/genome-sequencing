from itertools import combinations


AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

keys = [key for key in AminoAcidMass.keys()]
vals = [value for value in AminoAcidMass.values()]

for c in list(combinations(keys, 2)):
  sum = 0
  for e in c:
    sum += AminoAcidMass[e]
  
  if sum in vals:
    print(c, sum)