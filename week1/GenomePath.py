def genome_path(k_mers):
  strand = k_mers[0]
  print(k_mers)
  for i in range(1, len(k_mers)):
    print(k_mers[i])
    print(k_mers[i][-1])
    strand += k_mers[i][-1]
  
  return strand