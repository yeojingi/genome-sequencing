from queue import PriorityQueue

from .LinearPeptideScoring import linear_peptide_scoring
from .CycloPeptideScoring import cyclo_peptide_scoring
from .lib.Expand import expand
from .lib.Mass import mass
from .lib.CONSTANTS import AminoAcidMass

def leaderboard_cyclopeptide_sequencing(spectrum, N):
  leaderBoard = [""]
  leaderPeptides = []
  leaderScore = 0

  parentMass = spectrum[-1]

  while leaderBoard:
    leaderBoard = expand(leaderBoard)
    newLeaderBoard = PriorityQueue()
    for peptide in leaderBoard:
      if mass(peptide) == parentMass:
        if cyclo_peptide_scoring(peptide, spectrum) > leaderScore:
          leaderPeptides = [peptide]
          leaderScore = cyclo_peptide_scoring(peptide, spectrum)
        elif cyclo_peptide_scoring(peptide, spectrum) == leaderScore:
          leaderPeptides.append(peptide)
      elif mass(peptide) < parentMass:
        newLeaderBoard.put((-linear_peptide_scoring(peptide, spectrum), peptide))
    
    leaderBoard = []
    for _ in range(N):
      if newLeaderBoard.empty():
        break

      leaderBoard.append(newLeaderBoard.get()[1])

  # leaderPeptides.sort()

  # sortedPeptides = set()

  # for peptide in leaderPeptides:
  #   maxIndex = 0
  #   maxChar = peptide[0]
  #   for i in range(len(peptide)):
  #     if peptide[i] > maxChar:
  #       maxIndex = i
  #       maxChar = peptide[i]
    
  #   sortedPeptides.add( peptide[maxIndex:] + peptide[:maxIndex] )

  # leaderPeptides = list(sortedPeptides)
  # print(leaderPeptides, leaderScore, len(leaderPeptides))  
  ress = set()
  for leaderPeptide in leaderPeptides:
    res = []
    maxIndex = 0
    maxMass = AminoAcidMass[leaderPeptide[0]]

    for i in range(len(leaderPeptide)):
      m = AminoAcidMass[leaderPeptide[i]]
      res.append(m)

      if m > maxMass:
        maxMass = m
        maxIndex = i

    res = res[maxIndex:] + res[:maxIndex]

    ress.add("-".join(list(map(str, res))))

  print(len(ress))
  return "\n".join(list(ress))