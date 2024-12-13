import time
start_time = time.time()

def is_not_outside(pos):
  i = pos[0]
  j = pos[1]
  return i >= 0 and i < h and j >= 0 and j < w

def get_pos_key(pos):
  return f"{pos[0]}_{pos[1]}"

def get_key(pos, dir):
  return f"{pos[0]}_{pos[1]}_{dir}"

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

with open("day6_input.txt", "r") as file:
  text = file.read().split()

  w = len(text[0])
  h = len(text)

  obstacles = set()
  guard = [-1, -1]

  for i, line in enumerate(text):
    for j, char in enumerate(line):
      if char == '#':
        obstacles.add(get_pos_key([i, j]))
      elif char == '^':
        guard = [i, j]

  guard_start = guard.copy()
  guard_start_key = get_pos_key(guard_start)

  visited = set()
  direction = 0

  while is_not_outside(guard):
    visited.add(get_pos_key(guard))

    new_pos = get_new_position(guard, direction)
    while get_pos_key(new_pos) in obstacles:
      direction = change_direction(direction)
      new_pos = get_new_position(guard, direction)

    guard = new_pos
  
  # print(len(visited))

  potential_new_obstacles = set()
  for key in visited:
    if key == guard_start_key: continue
    potential_new_obstacles.add(key)

  # print(len(potential_new_obstacles))

  cycles = 0
  for obs in potential_new_obstacles:
    visited = set()
    new_obstacles = obstacles.union([obs])

    guard = guard_start.copy()
    direction = 0

    found_cycle = False
    while is_not_outside(guard):
      key = get_key(guard, direction)

      if key in visited:
        found_cycle = True
        break;

      visited.add(key)

      new_pos = get_new_position(guard, direction)
      while get_pos_key(new_pos) in new_obstacles:
        direction = change_direction(direction)
        new_pos = get_new_position(guard, direction)

      guard = new_pos

    if found_cycle:
      cycles += 1
    
  print("Count:", cycles)


end_time = time.time()
print(f"Vreme izvršavanja: {end_time - start_time:.2f} sekundi")