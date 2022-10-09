from re import A
from CONSTANTS import AminoAcidMass

def mass(peptide):
  ans = 0
  for aa in peptide:
    ans += AminoAcidMass[aa]
  
  return ans