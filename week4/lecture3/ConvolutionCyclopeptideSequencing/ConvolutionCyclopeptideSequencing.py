from .LeaderboardCyclopeptideSequencing_list import leaderboard_cyclopeptide_sequencing
from .SpectralConvolution import spectral_convolution


def convolution_cyclopeptide_sequencing(M, N, spectrum):
  spectrum.sort()

  Ms = spectral_convolution(M, spectrum)
  print('masses', Ms)
  
  res = leaderboard_cyclopeptide_sequencing(spectrum, N, Ms)

  return res