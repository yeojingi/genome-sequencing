from .lib.DeBrujinGraph import de_brujin_graph
from .EulerianPath import eulerian_path
from .lib.PathToGenome import path_to_genome

def string_reconstruction(k, k_mers):
  edges = de_brujin_graph(k, k_mers)
  path = eulerian_path(edges)
  text = path_to_genome(path, k_mers)

  return text