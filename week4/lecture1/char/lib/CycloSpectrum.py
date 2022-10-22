def cyclo_spectrum(peptide):
  AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

  masses = [0]
  L = len(peptide)
  cyclicPeptide = peptide*2
  for k in range(1, L):
    for i in range(L):
      window = cyclicPeptide[i:i+k]
      mass = 0

      for p in window:
        mass += AminoAcidMass[p]
      
      masses.append(mass)

  mass = 0

  for p in peptide:
    mass += AminoAcidMass[p]
  
  masses.append(mass)

  masses.sort()

  return masses

# print(cyclo_spectrum(input()))