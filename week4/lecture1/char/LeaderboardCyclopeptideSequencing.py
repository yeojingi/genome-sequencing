from queue import PriorityQueue

from .LinearPeptideScoring import linear_peptide_scoring
from .CycloPeptideScoring import cyclo_peptide_scoring
from .lib.Expand import expand
from .lib.Mass import mass
from .lib.CONSTANTS import AminoAcidMass

def leaderboard_cyclopeptide_sequencing(spectrum, N):
  leaderBoard = [""]
  leaderPeptide = ""
  parentMass = spectrum[-1]

  while leaderBoard:
    leaderBoard = expand(leaderBoard)
    newLeaderBoard = PriorityQueue()
    for peptide in leaderBoard:
      # print(peptide, mass(peptide), parentMass, '*' if mass(peptide) == parentMass else ' ')
      if mass(peptide) == parentMass:
        # print(peptide, leaderPeptide, cyclo_peptide_scoring(peptide, spectrum), cyclo_peptide_scoring(leaderPeptide, spectrum))
        if cyclo_peptide_scoring(peptide, spectrum) > cyclo_peptide_scoring(leaderPeptide, spectrum):
          leaderPeptide = peptide
        newLeaderBoard.put((-linear_peptide_scoring(peptide, spectrum), peptide))
      elif mass(peptide) < parentMass:
        newLeaderBoard.put((-linear_peptide_scoring(peptide, spectrum), peptide))
    
    leaderBoard = []
    for _ in range(N):
      if newLeaderBoard.empty():
        break

      leaderBoard.append(newLeaderBoard.get()[1])

  print(leaderPeptide)  
  res = []
  for i in range(len(leaderPeptide)):
    res.append(str(AminoAcidMass[leaderPeptide[i]]))

  return "-".join(res)