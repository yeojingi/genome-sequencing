def cyclo_spectrum(peptide):
  listPeptide = list(map(int, peptide.split('-')))
  masses = [0]
  L = len(listPeptide)
  cyclicPeptide = listPeptide + listPeptide

  for k in range(1, L):
    for i in range(L):
      window = cyclicPeptide[i:i+k]
      mass = sum(window)
      masses.append(sum(window))

  mass = sum(listPeptide)
  masses.append(mass)

  masses.sort()

  return masses

# print(cyclo_spectrum(input()))