def spectral_convolution(spectrum):
  convolutions = []

  L = len(spectrum)

  for i in range(L):
    for j in range(i+1, L):
      diff = spectrum[j] - spectrum[i]

      if diff > 0:
        convolutions.append(str(diff))
  
  return " ".join(convolutions)