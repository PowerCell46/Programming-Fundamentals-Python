strings = input()
strings1 = strings.split()
number = ""
first_letter = ""
last_letter = ""
counter = 0
total_sum = 0

for j in range(len(strings1)):
  for i in range(len(strings1[counter])):
    current = strings1[counter][i]
    if i == 0:
      first_letter = strings1[counter][i]

    if strings1[counter][i].isdigit():
      number += strings1[counter][i]

    if i == len(strings1[counter]) - 1:
      last_letter = strings1[counter][i]

  counter += 1  
  place1 = ord(first_letter.lower()) - 96
  place2 = ord(last_letter.lower()) - 96
  
  if first_letter.isupper():
    number = float(number) / place1
  else:
    number = float(number) * place1

  if last_letter.islower():
    number = float(number) + place2
  else:
    number = float(number) - place2

  total_sum += number
  
  number = ""

print(f"{total_sum:.2f}")  
