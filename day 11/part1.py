import time
start_time = time.time()

memo = [dict()] * 25
def stones_after_blinks(stones: list[int], blinks: int):
  n = len(stones)
  for q in range(0, blinks):
    updated = list()
    for i in range(n -1, -1, -1):
      if stones[i] == 0:
        updated.append(1)
        # stones[i] = 1
      else:
        s = str(stones[i])
        h, r = divmod(len(s), 2)
        if r == 0:
          left = int(s[0:h:])
          right = int(s[h::])

          updated.append(left)
          updated.append(right)
          # stones[i] = left
          # stones.append(right)
          n += 1
        else:
          updated.append(stones[i] * 2024)
          # stones[i] *= 2024
    stones = updated
  
  return stones

with open("testinput.txt", "r") as file:
  numbers = list(map(int, file.read().split(" ")))
  blinks = 25

  numbers = stones_after_blinks(numbers, blinks)
  print(len(numbers))


end_time = time.time()

# Ukupno vreme izvršavanja
execution_time = end_time - start_time
print(f"Vreme izvršavanja: {execution_time:.6f} sekundi")