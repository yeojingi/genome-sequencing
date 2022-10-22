def cyclization(peptides):
  newPeptides = set()

  for peptide in peptides:
    listPeptide = list(map(int, peptide.split('-')))
    maxI = 0
    maxV = listPeptide[0]
    for i in range(len(listPeptide)):
      if listPeptide[i] > maxV:
        maxV = listPeptide[i]
        maxI = i
    
    newPeptides.add("-".join(list(map(str, listPeptide[maxI:] + listPeptide[:maxI]))))
  
  return list(newPeptides)