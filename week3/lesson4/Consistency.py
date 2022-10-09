from CycloSpectrum import cyclo_spectrum
from LinearSpectrum import linear_spectrum

def cyclo_consistency(peptide, spectrum):
  spectrumOfPeptide = cyclo_spectrum(peptide)

  i = 0
  j = 0

  while i < len(spectrumOfPeptide):
    if j >= len(spectrum):
      return False

    if spectrumOfPeptide[i] < spectrum[j]:
      return False
    elif spectrumOfPeptide[i] > spectrum[j]:
      j += 1
    elif spectrumOfPeptide[i] == spectrum[j]:
      i += 1
      j += 1
  
  return True

def linear_consistency(peptide, spectrum):
  spectrumOfPeptide = linear_spectrum(peptide)

  i = 0
  j = 0

  while i < len(spectrumOfPeptide):
    if j >= len(spectrum):
      return False

    if spectrumOfPeptide[i] < spectrum[j]:
      return False
    elif spectrumOfPeptide[i] > spectrum[j]:
      j += 1
    elif spectrumOfPeptide[i] == spectrum[j]:
      i += 1
      j += 1

  return True