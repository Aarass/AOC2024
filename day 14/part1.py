import time
start_time = time.time()


import re
offset_r = r"\+(\d+),.*\+(\d+)"
prize_r = r"=(\d+),.*=(\d+)"

from typing import NamedTuple
class Coord(NamedTuple):
  x: int
  y: int

class State(NamedTuple):
  f: int
  coord: Coord
  
class NewState(NamedTuple):
  g: int
  h: int
  coord: Coord

import heapq

with open("input.txt", "r") as file:
  text = file.read().split("\n\n")
  tokens = 0
  clump_count = len(text)
  for nth, clump in enumerate(text):
    first, second, third = clump.splitlines()
    a = Coord(*tuple(map(int, re.findall(offset_r, first)[0])))
    b = Coord(*tuple(map(int, re.findall(offset_r, second)[0])))
    prize = Coord(*map(int, re.findall(prize_r, third)[0]))

    def h(c: Coord):
      return (pow(prize.x - c.x, 2) + pow(prize.y - c.y, 2)) ** 0.5

    g = dict()
    g[Coord(0, 0)] = 0
    processed = set[Coord]()
    to_be_processed_s = set[Coord]([Coord(0, 0)])
    to_be_processed = list[State]([State(0, Coord(0, 0))])

    def get_children(s: State):
      og = g[s.coord]
      na = Coord(s.coord.x + a.x, s.coord.y + a.y)
      nb = Coord(s.coord.x + b.x, s.coord.y + b.y)
      
      return [
        NewState(og + 3, h(na), na),
        NewState(og + 1, h(nb), nb)
      ]

    success = False
    while len(to_be_processed) > 0:
      current = heapq.heappop(to_be_processed)
      to_be_processed_s.remove(current.coord)

      # print(current)
      if current.coord == prize:
        success = True
        break
      
      if current.coord.x > prize.x or current.coord.y > prize.y:
        continue
        
      processed.add(current.coord)

      for child in get_children(current):
        if child.coord in processed:
          continue

        if child.coord not in to_be_processed_s:
          to_be_processed_s.add(child.coord)
          heapq.heappush(to_be_processed, State(child.g + child.h, child.coord))
          g[child.coord] = child.g
        else:
          for i in range(0, len(to_be_processed)):
            if child.coord == to_be_processed[i].coord:
              break

          if (child.g + child.h) < to_be_processed[i].f:
            to_be_processed[i] = State(child.g + child.h, child.coord)
            heapq.heapify(to_be_processed)
            g[child.coord] = child.g
      
    if success:
      tmp = g[current.coord]
      print("Tokens:", tmp)
      tokens += tmp
    else:
      print("No solution")
      pass

    print(f"{nth + 1}/{clump_count}")
  
  print(tokens)









end_time = time.time()
execution_time = end_time - start_time
print(f"Vreme izvršavanja: {execution_time:.6f} sekundi")