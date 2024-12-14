from itertools import combinations

with open("input.txt", "r") as file:
  text = file.read()
  # text = "2333133121414131402"

  id = 0
  blocks = list()

  for i, c in enumerate(text):
    val = int(c)
    if (i % 2) == 0:
      for j in range(0, val):
        blocks.append(id)
      id += 1
    else:
      for j in range(0, val):
        blocks.append(None)

  
  # before= " ".join(map(lambda x: str(x) if x is not None else '.', blocks))
  # print(before)

  count = len(blocks)
  left = 0
  right = count - 1

  while right > left:
    found_empty_spot = False
    while not found_empty_spot:
      if left >= count:
        break

      if blocks[left] == None:
        found_empty_spot = True
        break

      left += 1
    
    found_block = False
    while not found_block:
      if right < 0:
        break

      if blocks[right] != None:
        found_block = True
        break

      right -= 1
    
    if found_empty_spot and found_block and right > left:
      # print(blocks[right], f"[{right}] ↔ [{left}]")
      blocks[left], blocks[right] = blocks[right], blocks[left]
    
    left += 1
    right -= 1
  
  checksum = 0
  for i, block in enumerate(blocks):
    if block != None:
      checksum += i * block

  print(checksum)

  # print(before)
  # print(" ".join(map(lambda x: str(x) if x is not None else '.', blocks)))