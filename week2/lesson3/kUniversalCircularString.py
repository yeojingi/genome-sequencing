from lib.DeBrujinGraph import de_brujin_graph

def k_universal_circular_string(k):
  strings = []
  for i in range(2**k):
    string = "{0:b}".format(i)
    string = "0" * (k - len(string)) + string
    strings.append(string)

  edges = de_brujin_graph(k, strings)

  visited = [0] * len(strings)
  visited[0] = 1

  anss = []
  def rec(i, ans, k):
    # print(i, ans, k, edges[i], visited)
    if len(ans) == 2**k + (k-1):
      # print(visited)
      anss.append(ans[k-1:])
      print('this:', ans[k-1:])
      print(len(anss))
    
    flag = False
    for e in edges[i]:
      # print(visited)
      # print(binary_list[e][1:], ans[-3:])
      if visited[e] == 0 and strings[e][:-1] == ans[-(k-1):]:
        flag = True
        visited[e] = 1
        # print(i, e, edges[i][e])
        ans += strings[e][-1]
        rec(e, ans, k)
        visited[e] = 0
        ans = ans[:-1]
    
    return flag

  rec(0, strings[0], k)
  fo = open('./data/output.txt', 'w')
  fo.write("\n".join(anss))
  fo.close()
  
n = int(input())
k_universal_circular_string(n)