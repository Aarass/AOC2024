import re

with open("day3_input.txt", "r") as file:
  input_string = file.read()

  mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
  do_pattern = r"do\(\)"
  dont_pattern = r"don't\(\)"

  muls = re.finditer(mul_pattern, input_string)
  dos = re.finditer(do_pattern, input_string)
  donts = re.finditer(dont_pattern, input_string)

  sum = 0
  enabled = True

  next_do_index = -1
  next_dont_index = -1

  for match in muls:
    mul_start = match.start()
    # print(match)

    if next_do_index < mul_start:
      do_index = next_do_index
      while (value := next(dos, None)) is not None:
        if value.start() > mul_start:
          next_do_index = value.start()
          break;
        do_index = value.start()

    if next_dont_index < mul_start:
      dont_index = next_dont_index
      while (value := next(donts, None)) is not None:
        if value.start() > mul_start:
          next_dont_index = value.start()
          break;
        dont_index = value.start()

    print(str(do_index) + " " + str(dont_index) + " " + str(mul_start))
    if do_index >= dont_index:
      enabled = True
    else:
      enabled = False

    if enabled:
      l = match.group(1)
      r = match.group(2)

      print(l + " * " + r)

      sum += int(l) * int(r)

  print(sum)


    # print(match.start())




  # sum = 0
  # for match in matches:
  #   l = match.group(1)
  #   r = match.group(2)

  #   # print(match)
  #   # print(l)
  #   # print(r)

  #   sum += int(l) * int(r)


  # print(sum)