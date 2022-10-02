def path_to_genome(path, k_mers):
  ans = k_mers[path[0]]
  for i in range(1, len(path)):
    ans += k_mers[path[i]][-1]

  return ans