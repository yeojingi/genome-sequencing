from .lib.StringReconstruction import string_reconstruction
from .lib.FindStartEnd import find_start_end
from .lib.DeBrujinGraph import de_brujin_graph

def string_reconstruction_from_read_pairs(patterns, k, d):
  firstPatterns = []
  secondPatterns = []
  ans = ""

  for pattern in patterns:
    firstPattern, secondPattern = pattern.split('|')
    firstPatterns.append(firstPattern)
    secondPatterns.append(secondPattern)

  
  # firstEdges = de_brujin_graph(k, firstPatterns)
  # firstStartEnd = find_start_end(firstEdges)
  # print(firstStartEnd)
  
  prefixString = string_reconstruction(k, firstPatterns)
  suffixString = string_reconstruction(k, secondPatterns)

  print(prefixString)
  print(suffixString)

  for i in range(k+d, len(prefixString)):
    if prefixString[i] != suffixString[i - k - d]:
      return "there is no string spelled by the gapped patterns"
  ans = prefixString + suffixString[-(k+d):]
  return ans