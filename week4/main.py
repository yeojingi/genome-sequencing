from lecture3.SpectralConvolution import spectral_convolution
from lecture3.ConvolutionCyclopeptideSequencing.ConvolutionCyclopeptideSequencing import convolution_cyclopeptide_sequencing
from lecture1.char.LinearPeptideScoring import linear_peptide_scoring
from lecture1.char.CycloPeptideScoring import cyclo_peptide_scoring
from lecture3.SpectralConvolution import spectral_convolution

if __name__ == '__main__':
  # filename = input()
  # filename = "input.txt"
  # filename = "dataset_104_8.txt"
  # f = open(f"./lecture3/data/{filename}", "r")
  # M = int(f.readline().strip())
  # N = int(f.readline().strip())
  # spectrum = list(map(int, f.readline().strip().split()))
  # res = convolution_cyclopeptide_sequencing(M, N, spectrum)
  # print(res)
  # print(cyclo_peptide_scoring("MAMA", list(map(int, "0 57 71 71 71 104 131 202 202 202 256 333 333 403 404".split()))))
  res = spectral_convolution(list(map(int, "0 57 118 179 236 240 301".split())))
  s = {}
  for r in list(map(int, res.split())):
    if s.get(r):
      s[r] += 1
    else:
      s[r] = 1
  print(s)