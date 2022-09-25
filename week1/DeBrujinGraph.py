from OverlapGraph import overlap_graph


def de_brujin_graph(k, string):
  patterns = set()
  for i in range(len(string) - k + 2):
    patterns.add(string[i:i+k-1])
  
  edges = overlap_graph(list(patterns))

  return edges