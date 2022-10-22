def cyclo_spectrum(peptide):
  listPeptide = list(map(int, peptide.split('-')))
  masses = [0]
  L = len(listPeptide)
  cyclicPeptide = listPeptide + listPeptide
  for k in range(1, L):
    for i in range(L):
      mass = sum(cyclicPeptide[i:i+k])
      # mass = 0

      # for p in window:
      #   mass += AminoAcidMass[p]
      
      masses.append(mass)

  # mass = 0

  # for p in peptide:
  #   mass += AminoAcidMass[p]
  
  # masses.append(mass)

  masses.append(sum(listPeptide))

  masses.sort()

  return masses

# print(cyclo_spectrum(input()))