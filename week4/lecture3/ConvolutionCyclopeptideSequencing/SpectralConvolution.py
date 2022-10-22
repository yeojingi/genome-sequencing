def spectral_convolution(M, spectrum):
  convolutions = {}

  L = len(spectrum)

  for i in range(L):
    for j in range(i+1, L):
      diff = spectrum[j] - spectrum[i]

      if diff >= 57 and diff <= 200:
        if convolutions.get(diff):
          convolutions[diff] += 1
        else:
          convolutions[diff] = 1
  
  multiplicities = []

  for key, value in convolutions.items():
    multiplicities.append([key, value])
  
  multiplicities.sort(key=lambda x: x[1], reverse=True)

  valueM = multiplicities[M-1][1]
  print(multiplicities)

  res = []

  i = 0 
  while True:
    if multiplicities[i][1] >= valueM:
      res.append(multiplicities[i][0])
    else:
      break
    i += 1

  return res
