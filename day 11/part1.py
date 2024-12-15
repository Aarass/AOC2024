from functools import cache
import time
start_time = time.time()

def stones_after_blinks(stones: list[int], blinks: int):
  count = 0
  for stone in stones:
    count += stone_after_blinks(stone, blinks)
  
  return count

def get_children(stone: int):
  if stone == 0:
    return [1]
  else:
    s = str(stone)
    h, r = divmod(len(s), 2)
    if r == 0:
      left = int(s[0:h:])
      right = int(s[h::])

      return [left, right]
    else:
      return [stone * 2024]

@cache
def stone_after_blinks(stone: int, blinks: int):
  if blinks == 0:
    return 1

  new_stones = get_children(stone)

  count = 0
  for new_stone in new_stones:
    count += stone_after_blinks(new_stone, blinks - 1)
  
  return count

with open("input.txt", "r") as file:
  numbers = list(map(int, file.read().split(" ")))
  blinks = 75

  print(stones_after_blinks(numbers, blinks))


end_time = time.time()

# Ukupno vreme izvršavanja
execution_time = end_time - start_time
print(f"Vreme izvršavanja: {execution_time:.6f} sekundi")