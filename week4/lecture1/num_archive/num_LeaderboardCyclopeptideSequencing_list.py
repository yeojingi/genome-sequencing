from queue import PriorityQueue

from ..lib.CONSTANTS import AminoAcidMass

from .lib.num_LinearPeptideScoring import linear_peptide_scoring
from .lib.num_CycloPeptideScoring import cyclo_peptide_scoring
from .lib.num_Expand import expand
from .lib.num_Mass import mass
from .lib.num_cyclization import cyclization

def leaderboard_cyclopeptide_sequencing(spectrum, N):
  leaderBoard = list(map(str, AminoAcidMass.values()))
  leaderPeptides = []
  leaderScore = 0

  parentMass = spectrum[-1]

  while leaderBoard:
    leaderBoard = expand(leaderBoard) #
    
    newLeaderBoard = PriorityQueue()
    for peptide in leaderBoard:
      if mass(peptide) == parentMass: #
        if cyclo_peptide_scoring(peptide, spectrum) > leaderScore: #
          leaderPeptides = [peptide]
          leaderScore = cyclo_peptide_scoring(peptide, spectrum) #
        elif cyclo_peptide_scoring(peptide, spectrum) == leaderScore:
          leaderPeptides.append(peptide)
      elif mass(peptide) < parentMass:
        newLeaderBoard.put((-linear_peptide_scoring(peptide, spectrum), peptide)) #
    
    leaderBoard = []
    for _ in range(N):
      if newLeaderBoard.empty():
        break

      leaderBoard.append(newLeaderBoard.get()[1])

  
  
  print(len(leaderPeptides))
  leaderPeptides = cyclization(leaderPeptides)
  print(len(leaderPeptides))

  return leaderPeptides