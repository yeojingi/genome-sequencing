def string_spelled_by_gapped_patterns(patterns, k, d):
  firstPatterns = []
  secondPatterns = []

  for pattern in patterns:
    firstPattern, secondPattern = pattern.split('|')
    firstPatterns.append(firstPattern)
    secondPatterns.append(secondPattern)

  prefixString = string_reconstruction(k, firstPatterns)
  suffixString = string_reconstruction(k, secondPatterns)
  
  for i in range(k+d+1, len(prefixString)):
    if prefixString[i] != suffixString[i - (k + d) ]:
      return "there is no string spelled by the gapped patterns"

  return prefixString + suffixString[ len(prefixString) - k - d: ]


def string_reconstruction(k, patterns):
  ans = patterns[0]

  for i in range(1, len(patterns)):
    ans += patterns[i][-1]

  return ans
