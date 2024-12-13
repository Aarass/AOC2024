import time
start_time = time.time()

def is_not_outside(i, j):
  return i >= 0 and i < h and j >= 0 and j < w

def get_key(i, j):
  return f"{i}_{j}"

def visit(pos, direction):
  return (get_key(pos[0], pos[1]), direction)

def get_new_position(pos, direction):
  match direction:
    case 0:
      return [pos[0] - 1, pos[1]]
    case 1:
      return [pos[0], pos[1] + 1]
    case 2:
      return [pos[0] + 1, pos[1]]
    case 3:
      return [pos[0], pos[1] - 1]

def change_direction(direction):
  return (direction + 1) % 4

with open("day6_testinput.txt", "r") as file:
  text = file.read().split()

  w = len(text[0])
  h = len(text)

  obstacles = set()
  guard = [-1, -1]

  for i, line in enumerate(text):
    for j, char in enumerate(line):
      if char == '#':
        obstacles.add(get_key(i, j))
      elif char == '^':
        guard = [i, j]

  guard_start = guard.copy()

  visited = dict()
  direction = 0

  while is_not_outside(guard[0], guard[1]):
    key = get_key(guard[0], guard[1])
    if key not in visited:
      visited[key] = [(guard, direction)]
    else:
      visited[key].append((guard, direction))

    new_pos = get_new_position(guard, direction)
    while get_key(new_pos[0], new_pos[1]) in obstacles:
      # print("")
      direction = change_direction(direction)
      new_pos = get_new_position(guard, direction)

    guard = new_pos
  
  # print(len(visited))

  potential_new_obstacles = set()
  for key, visits in visited.items():
    for pos, dir in visits:
      if pos[0] == guard_start[0] and pos[1] == guard_start[1]:
        continue
      potential_new_obstacles.add(key)

  cycles = 0
  for obs in potential_new_obstacles:
    # new_obstacles = set(obstacles)
    # new_obstacles.add(obs)
    new_obstacles = obstacles.union([obs])

    visited = dict()
    direction = 0
    guard = guard_start.copy()

    found_cycle = False


    while is_not_outside(guard[0], guard[1]):
      key = get_key(guard[0], guard[1])
      if key not in visited:
        visited[key] = [(guard, direction)]
      else:
        # print("Check:", direction, visited[key])
        if direction in map(lambda x: x[1], visited[key]):
          found_cycle = True
          break;
        visited[key].append((guard, direction))

      new_pos = get_new_position(guard, direction)
      while get_key(new_pos[0], new_pos[1]) in new_obstacles:
        direction = change_direction(direction)
        new_pos = get_new_position(guard, direction)

      guard = new_pos

    if found_cycle:
      cycles += 1
      # print("Found cycle")
      # print(new_obstacles.difference(obstacles))

    
  print("Count:", cycles)


end_time = time.time()
print(f"Vreme izvršavanja: {end_time - start_time:.2f} sekundi")