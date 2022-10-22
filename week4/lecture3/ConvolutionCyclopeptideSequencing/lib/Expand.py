def expand(peptides, Masses):
  newPeptides = set()

  for peptide in peptides:
    for mass in Masses:
      # newPeptides.add(str(mass) + '-' + peptide)
      newPeptides.add(peptide + '-' + str(mass))
  
  return list(newPeptides)