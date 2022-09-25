binary_list = []
for i in range(16):
  binary_list.append('{0:04b}'.format(i))

def overlap_graph(patterns):
  edges = [ [] for _ in range(len(patterns))]

  for i in range(len(patterns)):
    tail = patterns[i][1:]
    for j in range(len(patterns)):
      head = patterns[j][:-1]

      if tail == head:
        edges[i].append(j)
  
  return edges

edges = overlap_graph(binary_list)

print(edges)
for i in range(len(binary_list)):
  v = [i]
  numV = 0
  visited = [0] * len(binary_list)
  visited[i] = 1
  anss = []

  def rec(i):
    for e in edges[i]:
      if visited[e] == 0:
        visited[e] = 1
        rec(e)
    
    anss.append(i)

  rec(i)
  
  def ss(e):
    return binary_list[e]
  anss.reverse()
  l = list(map(ss, anss))

  flag = True
  for i in range(1, len(l)):
    if l[i][1:] != l[i-1][:-1]:
      print(l[i][1:], l[i-1][:-1])
      flag = False
      break

  if flag:
    print(l[0], end="")
    for i in range(1, len(l)):
      print(l[i][-1],end="")
  # while v:
  #   cur = v.pop()
  #   numV += 1

  #   for e in edges[cur]:
  #     # print(v,cur,e)
  #     if visited[e] == 0:
  #       v.append(e)
  #       visited[e] = 1

  # print(i, numV)

  