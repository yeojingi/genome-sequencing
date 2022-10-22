from queue import PriorityQueue

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

  while leaderBoard:
    print(len(leaderBoard[0].split('-')), mass(leaderBoard[0]), parentMass)
    leaderBoard = expand(leaderBoard)
    newLeaderBoard = PriorityQueue()
    for peptide in leaderBoard:
      if mass(peptide) == parentMass:
        if cyclo_peptide_scoring(peptide, spectrum) > leaderScore:
          leaderPeptides = [peptide]
          leaderScore = cyclo_peptide_scoring(peptide, spectrum)
        elif cyclo_peptide_scoring(peptide, spectrum) == leaderScore:
          leaderPeptides.append(peptide)
        newLeaderBoard.put((-linear_peptide_scoring(peptide, spectrum), peptide))
      elif mass(peptide) < parentMass:
        newLeaderBoard.put((-linear_peptide_scoring(peptide, spectrum), peptide))
    
    leaderBoard = []
    for _ in range(N):
      if newLeaderBoard.empty():
        break

      leaderBoard.append(newLeaderBoard.get()[1])

    if len(leaderBoard) >= N:
      NthScore = -linear_peptide_scoring(leaderBoard[-1], spectrum)

      while True:
        (score, peptide) = newLeaderBoard.get()
        if score != NthScore:
          break
        leaderBoard.append(peptide)

  s = set(leaderPeptides)
  print(len(leaderPeptides))
  print(len(s))
  return " ".join(list(s))