from itertools import pairwise

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def is_safe(elements):
  sdiff = int(elements[1]) - int(elements[0])
  ssign = sign(sdiff)

  if (abs(sdiff) < 1 or abs(sdiff) > 3): return False

  if all(
    (sign((diff := (int(y) - int(x)))) == ssign) and
    (1 <= abs(diff) <= 3)
    for x, y in pairwise(elements[1::])
  ):
    return True
  else:
    return False



with open("day2_input.txt", "r") as file:
  count = 0
  for line in file:
    if (is_safe(line.split())):
      count = count + 1

  print(count)

