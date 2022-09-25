def overlap_graph(patterns):
  adjacents = [ [] for _ in range(len(patterns))]

  for i in range(len(patterns)):
    tail = patterns[i][1:]
    for j in range(len(patterns)):
      head = patterns[j][:-1]

      if tail == head:
        adjacents[i].append(patterns[j])
  
  anss = []
  for i in range(len(patterns)):
    if not adjacents[i]:
      continue

    ans = f"{patterns[i]}: "
    ans += " ".join(adjacents[i])
    anss.append(ans)

  return "\n".join(anss)