from CONSTANTS import AminoAcidMass
from Expand import expand
from Mass import mass
from Consistency import linear_consistency, cyclo_consistency

def cyclo_peptide_sequencing(spectrum):
  spectrum.sort()

  FinalPeptides = []
  parentMass = spectrum[-1]
  CandidatePeptides = [key for key in AminoAcidMass.keys()]

  while CandidatePeptides:
    CandidatePeptides = expand(CandidatePeptides)
    NewCandidatePeptides = []

    for peptide in CandidatePeptides:
      # print(peptide, mass(peptide))
      if mass(peptide) == parentMass:
        massList = [str(AminoAcidMass[aa]) for aa in peptide]
        massString = "-".join(massList)
        if cyclo_consistency(peptide, spectrum) and massString not in FinalPeptides:
          FinalPeptides.append(massString)

      elif linear_consistency(peptide, spectrum):
        NewCandidatePeptides.append(peptide)

    CandidatePeptides = NewCandidatePeptides
  #   print(CandidatePeptides, parentMass)

  # print(CandidatePeptides)
  # print(FinalPeptides)
  return FinalPeptides

    

# name = "Tyrocidine_B1_theoretical_spectrum.txt"
name = input()
f = open(f"./data/{name}", 'r')
string = f.readline().strip()
masses = list(map(int, string.split(' ')))
print(cyclo_peptide_sequencing(masses))