from .CONSTANTS import AminoAcidMass

def mass(peptide):
  return sum(list(map(int, peptide.split('-'))))