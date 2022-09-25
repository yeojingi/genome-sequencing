from Composition import composition
from GenomePath import genome_path
from OverlapGraph import overlap_graph
from DeBrujinGraph import de_brujin_graph
from DeBrujinGraphFromKMers import de_brujin_graph_from_k_mers


filename = input()
f = open(f'./data/{filename}', 'r')
# k = int(f.readline()[:-1])
k_mers = f.readline()[:-1].split(' ')
ans = de_brujin_graph_from_k_mers(k_mers)
f.close()

fo = open('./data/output.txt', 'w')
fo.write(ans)
fo.close()