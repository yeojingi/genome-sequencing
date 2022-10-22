def linear_spectrum(peptide):
  masses = [0]
  L = len(peptide)
  listPeptide = list(map(int, peptide.split('-')))

  for k in range(1, L+1):
    for i in range(L-k+1):
      window = listPeptide[i:i+k]
      mass = sum(window)
      
      masses.append(mass)

  masses.sort()

  return masses

