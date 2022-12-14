from .LinearSpectrum import linear_spectrum

def linear_peptide_scoring(peptide, spectrum):
  score = 0
  matched = []

  peptide_spectrum = linear_spectrum(peptide)
  # peptide_spectrum = list(map(int, "0 97 244".split()))

  s = 0
  for mass in peptide_spectrum:
    if s >= len(spectrum):
      continue
  
    while spectrum[s] < mass:
      if s >= len(spectrum):
        break
      s += 1

    if spectrum[s] > mass:
      continue
    elif spectrum[s] == mass:
      s += 1
      score += 1
      matched.append(mass)
  # print(peptide)
  # print(peptide_spectrum)
  # print(spectrum)
  # print(matched)
  # print(score)
  
  return score

# print(linear_peptide_scoring("", list(map(int, "0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322".split()))))
