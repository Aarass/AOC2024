from itertools import pairwise

with open("day1_input.txt", "r") as file:
  data = file.read().split()

  list1 = data[::2]
  list2 = data[1::2]

  occurrences = dict()

  for el in list2:
    occurrences[el] = 1 if occurrences.get(el) is None else (occurrences.get(el) + 1)

  print(list1)
  print(occurrences)

  similarities = [0 if occurrences.get(el) is None else int(occurrences.get(el)) * int(el) for el in list1]

  res = sum(similarities)

  print(similarities)
  print(res)