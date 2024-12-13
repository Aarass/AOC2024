import re

with open("day4_input.txt", "r") as file:
  first_line = next(file)
  input_string = first_line + file.read()

  step = len(first_line)
  skip_dl = r"[^ ]{" + str(step -3) + r"}[^$]"

  regs = [
    r"(M).(M)" + skip_dl + r"(A)" + skip_dl + r"(S).(S)",
    r"(M).(S)" + skip_dl + r"(A)" + skip_dl + r"(M).(S)",
    r"(S).(M)" + skip_dl + r"(A)" + skip_dl + r"(S).(M)",
    r"(S).(S)" + skip_dl + r"(A)" + skip_dl + r"(M).(M)",
  ]

  count = 0

  for reg in regs:
    s = input_string
    while (match := next(re.finditer(reg, s), None)) is not None:
      s = s[match.start() + 1::]

      count += 1

  print(count)

def printMatch(match):
  lines = match.group().split()
  for l in lines[0:-1:]:
    print(l.rjust(step-1))
  print(lines[-1])