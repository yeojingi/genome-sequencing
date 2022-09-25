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
print(binary_list)
v = [0]
numV = 0
visited = [0] * len(binary_list)
visited[0] = 1
ans = "0000"

def rec(i):
  global ans
  if len(ans) == 19:
    # print(visited)
    print(ans)
  
  flag = False
  for e in edges[i]:
    # print(visited)
    # print(binary_list[e][1:], ans[-3:])
    if visited[e] == 0 and binary_list[e][:3] == ans[-3:]:
      flag = True
      visited[e] = 1
      # print(i, e, edges[i][e])
      ans += binary_list[e][-1]
      rec(e)
      visited[e] = 0
      ans = ans[:-1]
  
  return flag

rec(0)
