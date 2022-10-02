# from lesson2.EulerianCycle import eulerian_cycle
# from lesson2.EulerianPath import eulerian_path
# from lesson2.StringReconstruction import string_reconstruction
from lesson5.StringSpelledByGappedPatterns import string_spelled_by_gapped_patterns
from lesson3.StringReconstructionFromReadPairs import string_reconstruction_from_read_pairs
from lesson4.Contigs import generate_contigs


filename = input()
f = open(f"./lesson4/data/{filename}", 'r')
k_mers = f.readline()[:-1].split(' ')
f.close()
output = generate_contigs(k_mers)
print(output)

# fo = open("./lesson2/data/output.txt", "w")
# fo.write(output)
# fo.close()