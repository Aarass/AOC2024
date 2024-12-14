from collections import namedtuple


Block = namedtuple("Block", ["type", "size", "id"])
with open("input.txt", "r") as file:
  text = file.read().strip()
  # text = "2333133121414131402"

  # File(0, 1024, None)
  blocks = list[Block]()

  id = 0
  index = 0
  for i, c in enumerate(text):
    val = int(c)
    if (i % 2) == 0:
      blocks.append(Block(1, val, id))
      id += 1
    else:
      blocks.append(Block(0, val, '.'))
    index += val
  
  # s = ""
  # for block in blocks:
  #   s += str(block.id) * block.size
  # print(s)


  n = len(blocks)
  for i in range(n -1, -1, -1):
    if blocks[i].type == 0: continue
    file = blocks[i]

    for j in range(0, n):
      if blocks[j].type == 1: continue
      free = blocks[j]


      if j > i: break

      if file.size <= free.size:
        leftover = None
        if file.size < free.size:
          leftover = Block(0, free.size - file.size, '.')

        blocks[j] = Block(1, file.size, file.id)
        blocks[i] = Block(0, file.size, '.')

        # s = ""
        # for block in blocks:
        #   s += str(block.id) * block.size
        #   s += '|'
        # print(s)

        current_index = i
        if ((current_index -1) >= 0) and blocks[current_index -1].type == 0:
          current_free = blocks[current_index]
          previous_free = blocks.pop(current_index -1)

          n -= 1
          current_index -= 1

          blocks[current_index] = Block(0, previous_free.size + current_free.size, '.')
          pass

        # s = ""
        # for block in blocks:
        #   s += str(block.id) * block.size
        #   s += '|'
        # print(s)

        if ((current_index +1) < n) and blocks[current_index +1].type == 0:
          current_free = blocks[current_index]
          next_free = blocks.pop(current_index +1)
          n -= 1
          blocks[current_index] = Block(0, current_free.size + next_free.size, '.')
          pass

        # s = ""
        # for block in blocks:
        #   s += str(block.id) * block.size
        #   s += '|'
        # print(s)

        if leftover != None:
          # print(leftover, j)
          blocks.insert(j + 1, leftover)

        # s = ""
        # for block in blocks:
        #   s += str(block.id) * block.size
        #   s += '|'
        # print(s)

 



        break

    
        
  # print("-------------------------------------------------------------------------------------------------------------------------------------------")
  # s = ""
  # for block in blocks:
  #   s += str(block.id) * block.size
  #   s += '|'
  # print(s)

  checksum = 0
  i = 0
  for block in blocks:
    if block.type == 1:
      for j in range(0, block.size):
        checksum += i * block.id
        i += 1
    else:
      i += block.size

  
  print(checksum)