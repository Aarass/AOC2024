import time
start_time = time.time()









from typing import NamedTuple, Iterator
from itertools import pairwise

class Coord(NamedTuple):
  i: int
  j: int

class Neighbour(NamedTuple):
  value: int
  coord: Coord

class Fence(NamedTuple):
  coord: Coord
  normal: tuple


with open("input.txt", "r") as file:
  text = list[list]()
  for line in file:
    text.append(list(line.strip()))

  w = len(text[0])
  h = len(text)

  def coord_to_neighbour(c: Coord) -> Neighbour:
    if c.i < 0 or c.i >= h or c.j < 0 or c.j >= w:
      return Neighbour(None, c)
    return Neighbour(text[c.i][c.j], c)

  def get_neighbours(c: Coord) -> Iterator[Neighbour]:
    return map(coord_to_neighbour, [
       Coord(c.i -1, c.j),
       Coord(c.i +1, c.j),
       Coord(c.i, c.j -1),
       Coord(c.i, c.j +1),
    ])
  
  cost = 0

  finished = set()

  to_be_visited = set([Coord(0, 0)])

  while len(to_be_visited) > 0:
    current_start = to_be_visited.pop()
    area = 0

    current_region = set()
    fences = list[Fence]()

    to_be_processed = set([current_start])
    while len(to_be_processed) > 0:
      current = to_be_processed.pop()
      current_value = text[current.i][current.j]

      area += 1
      current_region.add(current)
      finished.add(current)

      # if text[current_start.i][current_start.j] == 'B':
      #   print(current, current_value, to_be_processed)

      neighbours = get_neighbours(current)

      # print("Value:", current_value, "Coord:", current)

      for n in neighbours:
        if n.coord in to_be_visited:
          to_be_visited.remove(n.coord)

        if n.value != current_value:
          # Fence
          # ---------------
          fences.append(Fence(n.coord, (n.coord.i - current.i, n.coord.j - current.j)))

          # ---------------


          if n.value != None and n.coord not in finished:
              to_be_visited.add(n.coord)
        else:
          if n.coord not in current_region:
            to_be_processed.add(n.coord)
    
    # print(f"Region starting at {current_start}, {text[current_start.i][current_start.j]}, has Area:", area, "Perimeter:", perimeter)
    # print(current_region)

    # print(f"{text[current_start.i][current_start.j]}")
    fences.sort(key = lambda fence: (fence.normal, fence.coord[0], fence.coord[1]) if fence.normal[1] == 0 else (fence.normal, fence.coord[1], fence.coord[0]))


    # if current_value == 'R':
    #   for f in fences:
    #     print(f)

    keeper = list()

    perimeter = 1
    for (f1, f2) in pairwise(fences):
      if f1.normal != f2.normal:
        perimeter += 1
        keeper.append(f1)
        continue


      normal = f1.normal
      match normal:
        case (0, 1) | (0, -1):
          if f2.coord.i - f1.coord.i != 1 or f2.coord.j != f1.coord.j:
            perimeter += 1
            keeper.append(f1)
            continue
        case (1, 0) | (-1, 0):
          if f2.coord.j - f1.coord.j != 1 or f2.coord.i != f1.coord.i:
            perimeter += 1
            keeper.append(f1)
            continue

    # print(current_value, perimeter)
    # for f in keeper:
    #   print(f)


    cost += area * perimeter
  print(cost)

    


    # print(f"Current start: {text[current_start.i][current_start.j]} -> {current_start}")











end_time = time.time()
execution_time = end_time - start_time
print(f"Vreme izvršavanja: {execution_time:.6f} sekundi")