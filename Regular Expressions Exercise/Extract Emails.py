import re
 
strings = input()
regex = r"\b(?![_.-])(?<![-.])[a-zA-Z0-9-._]+@[A-Za-z-]+\.[A-Za-z-\.]+\b"
final = re.findall(regex, strings)
 
for i in range(len(final)):
  matches = final[i]
 
  if i == len(final) - 1:
    print(matches)
  else:
    print(matches, end="\n")
