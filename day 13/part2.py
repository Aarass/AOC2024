import time
start_time = time.time()

import re
offset_r = r"\+(\d+),.*\+(\d+)"
prize_r = r"=(\d+),.*=(\d+)"

from typing import NamedTuple
class Coord(NamedTuple):
  x: int
  y: int

import numpy as np

with open("input.txt", "r") as file:
  text = file.read().split("\n\n")
  tokens = 0
  clump_count = len(text)
  for nth, clump in enumerate(text):
    first, second, third = clump.splitlines()
    a = Coord(*tuple(map(int, re.findall(offset_r, first)[0])))
    b = Coord(*tuple(map(int, re.findall(offset_r, second)[0])))
    prize = Coord(*map(lambda x: int(x), re.findall(prize_r, third)[0]))
    prize = Coord(prize.x + 10000000000000, prize.y + 10000000000000)


    A = np.array([[a.x, b.x], 
                  [a.y, b.y]])
    A_inv = np.linalg.inv(A)
    ax, bx = A_inv[0]
    ay, by = A_inv[1]

    x = prize.x * ax + prize.y * bx
    y = prize.x * ay + prize.y * by

    ix = round(x)
    iy = round(y)

    rx = ix * a.x + iy * b.x
    ry = ix * a.y + iy * b.y

    if rx == prize.x and ry == prize.y:
      tokens += 3 * ix + iy

  print(tokens)











end_time = time.time()
execution_time = end_time - start_time
print(f"Vreme izvršavanja: {execution_time:.6f} sekundi")