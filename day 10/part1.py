with open("input.txt", "r") as file:
  zeros = list()
  nodes = list()
  for i, line in enumerate(file):
    line = list(line.strip())
    nodes.append(line)
    for j, ch in enumerate(line):
      if ch == '0':
        zeros.append((j, i))

  h = len(nodes)
  w = len(nodes[0])

  def is_in_bounds(pos: tuple[int, int]):
    x, y = pos
    return x >= 0 and x < w and y >= 0 and y < h

  def get_neightbours(x, y):
    return filter(is_in_bounds, [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)])

  def slope_check(current_value: int, n: tuple[int, int]):
    tmp = nodes[n[1]][n[0]]
    if tmp == '.': return False
    val = int(tmp)
    if val - current_value == 1:
      return True
    return False

  paths = 0
  for zero in zeros:
    nines = set()
    nodes_to_process = [zero]
    while len(nodes_to_process) > 0:
      x, y = nodes_to_process.pop()
      current_value = int(nodes[y][x])

      if current_value == 9:
        nines.add((x, y))

      neighbours = get_neightbours(x, y)
      valid_neighbours = [n for n in neighbours if slope_check(current_value, n)]

      # print(current_value, list(map(lambda el: (el, nodes[el[1]][el[0]]), valid_neighbours)))

      nodes_to_process.extend(valid_neighbours)
    
    paths += len(nines)
  
  print(paths)
