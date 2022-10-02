from copy import deepcopy

from .lib.Degrees import degrees

from .lib.DeBrujinGraph import de_brujin_graph


def generate_contigs(patterns):
  contigs = []

  k = len(patterns[0])
  edges = de_brujin_graph(k, patterns)
  degs = degrees(edges)
  
  print(edges)
  print(degs)

  return contigs