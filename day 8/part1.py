from itertools import combinations

def caclulate_antinodes(a: tuple, b: tuple, constraint):
  stopped = False

  res = [a]

  while not stopped:
    di = b[0] - a[0]
    dj = b[1] - a[1]

    new = (b[0] + di, b[1] + dj)

    if (constraint(new)):
      res.append(new)
      a = b
      b = new
    else:
      break;

  return res

def is_in_bounds(node: tuple, w, h):
  i = node[0]
  j = node[1]
  return i >= 0 and i < h and j >= 0 and j < w


with open("input.txt", "r") as file:
# with open("testinput.txt", "r") as file:
  text = file.read().split()
  w = len(text[0])
  h = len(text)

  antennas = dict()

  for i, line in enumerate(text):
    for j, char in enumerate(line):
      if char == '.': continue

      if char not in antennas:
        antennas[char] = [(i, j)]
      else:
        antennas[char].append((i, j))


  antinodes = set()

  for positions in antennas.values():
    for combination in combinations(positions, 2):
      constraint = lambda node: is_in_bounds(node, w, h)
      new_antinodes = caclulate_antinodes(combination[0], combination[1], constraint) + caclulate_antinodes(combination[1], combination[0], constraint)
      # in_bounds_antinodes = filter(lambda node: is_in_bounds(node, w, h), new_antinodes)
      antinodes.update(new_antinodes)
  
  print(antinodes)
  print(len(antinodes))