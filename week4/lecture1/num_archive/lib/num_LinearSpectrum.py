def linear_spectrum(peptide):
  AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

  listPeptide = list(map(int, peptide.split('-')))
  masses = [0]
  L = len(listPeptide)

  for k in range(1, L+1):
    for i in range(L-k+1):
      mass = sum(list(map(int, listPeptide[i:i+k])))
      # mass = 0

      # for p in window:
      #   mass += AminoAcidMass[p]
      
      masses.append(mass)

  masses.sort()

  return masses
