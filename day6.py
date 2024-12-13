def get_key(i, j):
  return f"{i}_{j}"


with open("day6_input.txt", "r") as file:
  text = file.read().split()

  w = len(text[0])
  h = len(text)

  print(f"{w}x{h}")

  def is_not_outside(i, j):
    return i >= 0 and i < h and j >= 0 and j < w

  for line in text:
    print(line)
  print()

  obstacles = set()
  guard = [-1, -1]

  for i, line in enumerate(text):
    for j, char in enumerate(line):
      if char is '#':
        obstacles.add(get_key(i, j))
      elif char is '^':
        guard = [i, j]

  for el in obstacles:
    print(el)
  print(guard)

  visited = set()
  direction = 0

  def get_new_position():
    match direction:
      case 0:
        return [guard[0] - 1, guard[1]]
      case 1:
        return [guard[0], guard[1] + 1]
      case 2:
        return [guard[0] + 1, guard[1]]
      case 3:
        return [guard[0], guard[1] - 1]

  def change_direction():
    global direction
    direction = (direction + 1) % 4

  while is_not_outside(guard[0], guard[1]):
    visited.add(get_key(guard[0], guard[1]))

    new_pos = get_new_position()
    while get_key(new_pos[0], new_pos[1]) in obstacles:
      change_direction()
      new_pos = get_new_position()

    # print(new_pos)
    guard = new_pos
  
  print(len(visited))




