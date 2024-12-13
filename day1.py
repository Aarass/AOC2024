from itertools import pairwise

with open("day1_input.txt", "r") as file:
  data = file.read().split()

  list1 = sorted(data[::2])
  list2 = sorted(data[1::2])

  diffs = [abs(int(x) - int(y)) for x, y in zip(list1, list2)]
  res = sum(diffs)

  print(res)