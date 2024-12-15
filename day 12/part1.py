import time
start_time = time.time()









from typing import NamedTuple, Iterator

class Coord(NamedTuple):
    i: int
    j: int

class Neighbour(NamedTuple):
    value: int
    coord: Coord

with open("input.txt", "r") as file:
  text = list[list]()
  for line in file:
    text.append(list(line.strip()))

  w = len(text[0])
  h = len(text)

  def coord_to_neighbour(c: Coord) -> Neighbour:
    if c.i < 0 or c.i >= h or c.j < 0 or c.j >= w:
      return Neighbour(None, None)
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
    perimeter = 0

    current_region = set()

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
          if n.value == None:
            perimeter += 1
          else:
            perimeter += 1
            if n.coord not in finished:
              to_be_visited.add(n.coord)
        else:
          if n.coord not in current_region:
            to_be_processed.add(n.coord)
    
    # print(f"Region starting at {current_start}, {text[current_start.i][current_start.j]}, has Area:", area, "Perimeter:", perimeter)
    # print(current_region)

    cost += area * perimeter
  print(cost)

    


    # print(f"Current start: {text[current_start.i][current_start.j]} -> {current_start}")











end_time = time.time()
execution_time = end_time - start_time
print(f"Vreme izvršavanja: {execution_time:.6f} sekundi")