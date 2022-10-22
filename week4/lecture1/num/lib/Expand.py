from .CONSTANTS import Masses

def expand(peptides):
  newPeptides = []

  for peptide in peptides:
    for mass in Masses:
      newPeptides.append(str(mass) + '-' + peptide)
      newPeptides.append(peptide + '-' + str(mass))
  
  return newPeptides