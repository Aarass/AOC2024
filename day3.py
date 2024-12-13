import re

with open("day3_input.txt", "r") as file:
  input_string = file.read()
  pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

  matches = re.finditer(pattern, input_string)
  sum = 0
  for match in matches:
    l = match.group(1)
    r = match.group(2)

    # print(match)
    # print(l)
    # print(r)

    sum += int(l) * int(r)


  print(sum)



