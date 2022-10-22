from queue import PriorityQueue

from .lib.Trim import trim

from .LinearPeptideScoring import linear_peptide_scoring
from .CycloPeptideScoring import cyclo_peptide_scoring
from .lib.Expand import expand
from .lib.Mass import mass
from .lib.CONSTANTS import AminoAcidMass, Masses

def leaderboard_cyclopeptide_sequencing(spectrum, N):
  leaderBoard = list(map(str, Masses))
  leaderPeptides = []
  leaderScore = 0

  parentMass = spectrum[-1]
  print("num2")

  while leaderBoard:
    print(len(leaderBoard[0].split('-')), 'leaderScore', leaderScore, '# of leaderPeptides', len(leaderPeptides), 'leaderBoard', len(leaderBoard))
    leaderBoard = expand(leaderBoard)
    newLeaderBoard = []

    for peptide in leaderBoard:
      if mass(peptide) == parentMass:
        if cyclo_peptide_scoring(peptide, spectrum) > leaderScore:
          leaderPeptides = [peptide]
          leaderScore = cyclo_peptide_scoring(peptide, spectrum)
        elif cyclo_peptide_scoring(peptide, spectrum) == leaderScore:
          leaderPeptides.append(peptide)
        newLeaderBoard.append(peptide)
        # print("여긴 오지도 않잖아")
      elif mass(peptide) < parentMass:
        newLeaderBoard.append(peptide)
    
    leaderBoard = trim(newLeaderBoard, spectrum, N)

  s = set(leaderPeptides)
  print(len(leaderPeptides))
  print(len(s))
  return " ".join(list(leaderPeptides))