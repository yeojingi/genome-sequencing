def composition(k, text):
  k_mers = []
  for i in range(len(text) - k + 1):
    k_mers.append(text[i:i+k])

  # k_mers.sort()
  return k_mers
