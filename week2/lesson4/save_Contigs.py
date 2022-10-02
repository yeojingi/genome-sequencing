from copy import deepcopy


def generate_contigs(patterns):
  contigs = []

  k = len(patterns[0])
  i = 0
  string = patterns[0]
  patterns.remove(string)

  while len(patterns) > 0:

    if string[1:] == patterns[i][:-1]:
      string += patterns[i][-1]
      patterns.remove(string[-k:])
      i = 0
    else:
      i += 1

    if i >= len(patterns):
      i = 0
      contigs.append(string)
      string = patterns[0]
      patterns.remove(string)

  return contigs