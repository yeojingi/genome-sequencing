def de_brujin_graph_from_k_mers(k_mers):
  H = {}
  for k_mer in k_mers:
    if not H.get(k_mer[:-1]):
      H[k_mer[:-1]] = [k_mer[1:]]
    else:
      H[k_mer[:-1]].append(k_mer[1:])
  
  string = ""
  for key, value in H.items():
    string += f"{key}: "
    string += " ".join(value)
    string += "\n"

  return string