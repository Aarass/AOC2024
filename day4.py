import re
import textwrap

with open("day4_input.txt", "r") as file:
  first_line = next(file)
  input_string = first_line + file.read()

  step = len(first_line)

  skip_dd = r"[^\n][^ ]{" + str(step -1) + r"}"
  skip_dl = r"[^ ]{" + str(step -3) + r"}[^$]"
  skip_v = r"[^ ]{" + str(step -1) + r"}"



  regs = [
    r"(X)(M)(A)(S)",
    r"(S)(A)(M)(X)",
    r"(X)" + skip_dd + r"(M)" + skip_dd + r"(A)" + skip_dd + r"(S)",
    r"(S)" + skip_dd + r"(A)" + skip_dd + r"(M)" + skip_dd + r"(X)",
    r"(X)" + skip_dl + r"(M)" + skip_dl + r"(A)" + skip_dl + r"(S)",
    r"(S)" + skip_dl + r"(A)" + skip_dl + r"(M)" + skip_dl + r"(X)",
    r"(X)" + skip_v + r"(M)" + skip_v + r"(A)" + skip_v + r"(S)",
    r"(S)" + skip_v + r"(A)" + skip_v + r"(M)" + skip_v + r"(X)",
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