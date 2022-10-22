from .lib.CycloSpectrum import cyclo_spectrum

def cyclo_peptide_scoring(peptide, spectrum):
  score = 0

  peptide_spectrum = cyclo_spectrum(peptide)

  s = 0
  for mass in peptide_spectrum:
    if s >= len(spectrum):
      continue
  
    while spectrum[s] < mass:
      if s >= len(spectrum):
        break
      s += 1

    if spectrum[s] > mass:
      continue
    else:
      s += 1
      score += 1
  
  return score