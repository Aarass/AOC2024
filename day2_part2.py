from day2 import is_safe

with open("day2_input.txt", "r") as file:
  count = 0
  for line in file:
    elements = line.split()
    sublists = [elements[:i] + elements[i+1:] for i in range(len(elements))]
    sublists.insert(0, elements)

    for list in sublists:
      if (is_safe(list)):
        count = count + 1
        break

  print(count)
