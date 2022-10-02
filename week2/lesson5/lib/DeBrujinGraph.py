def de_brujin_graph(k, k_mers):
  # k_mer_int = { k_mers[i]: i for i in range(len(k_mers)) }
  edges = {}
  
  for i in range(len(k_mers)):
    for j in range(len(k_mers)):
      start = k_mers[i]
      end = k_mers[j]

      if start[1:] == end[:-1]:
        if not edges.get(i):
          edges[i] = [j]
        else:
          edges[i].append(j)
  print(edges)

  return edges