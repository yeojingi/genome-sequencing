def k_d_mer(k, d, text):
  anss = []
  first = ""
  second = ""
  for i in range(len(text) - (k+d) + 1):
    first = text[i:i+k]
    second = text[i + k + d: i+ d + k + k]
    anss.append(f"({first}|{second})")
  
  anss.sort()
  return " ".join(anss)

s = input()
print(k_d_mer(3, 2, s))