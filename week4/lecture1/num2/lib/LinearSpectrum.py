def linear_spectrum(peptide):
  masses = [0]
  listPeptide = list(map(int, peptide.split('-')))
  L = len(listPeptide)

  for k in range(1, L+1):
    for i in range(L-k+1):
      window = listPeptide[i:i+k]
      mass = sum(window)
      
      masses.append(mass)

  masses.sort()

  if len(masses) != L * (L+1) / 2 + 1:
    print('wowowfeoifw')
    exit()
  return masses

print(linear_spectrum("129-113-147-137"))