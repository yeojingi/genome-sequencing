s = "000010001100111010100101101111100000"

strings = []
k= 5
for i in range(2**k):
  string = "{0:b}".format(i)
  string = "0" * (k - len(string)) + string
  strings.append(string)

print(strings)
for i in range(len(s) - k + 1):
  strings.remove( s[i:i+k] )

print(strings)
print(len(s))