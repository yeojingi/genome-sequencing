# from ..LinearScoring import linear_scoring
# from ...lecture5.Trim.LinearScoring import linear_scoring

from .LinearSpectrum import linear_spectrum
from .LinearPeptideScoring import linear_peptide_scoring
from copy import copy


def trim(leaderboard, spectrum, N):
  linearScore = []
  trimmed = []

  for i in range(len(leaderboard)):
    peptide = leaderboard[i]
    
    linearScore.append([linear_peptide_scoring(peptide, spectrum), peptide])
  
  # 오름차순
  linearScore.sort(key=lambda x: x[0])

  if len(linearScore) < N:
    return leaderboard

  else:
    criteriaScore = linearScore[-N][0]

  while linearScore and linearScore[-1][0] >= criteriaScore:
    trimmedSignle = linearScore.pop()
    trimmed.append(trimmedSignle[1])
  
  print(linearScore[-1], trimmedSignle, len(trimmed), trimmed[N], criteriaScore)
  print('leaderBoard size', len(leaderboard), 'cutoff', len(leaderboard) - len(trimmed))# criteriaScore, len(linearScore), len(trimmed), len(leaderboard))
  
  return trimmed

def linear_scoring(peptide, spectrum):
  peptide = list(map(int, peptide.split('-')))
  L = len(peptide)
  spectrum = copy(spectrum)
  S = len(spectrum)

  def mass(window):
    ans = 0
    
    for aa in window:
      ans += aa
    
    return ans

  for k in range(L+1):
    for i in range(L - k + 1):
      window = peptide[i:i+k]
      m = mass(window)

      try:
        spectrum.remove(m)
      except ValueError as e:
        pass
      
  
  ans = S - len(spectrum)
  
  return ans