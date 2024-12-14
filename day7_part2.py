def count_up(arr, base):
  for i in range(len(arr) -1, -1, -1):
    val = arr[i] + 1
    if val == base:
      arr[i] = 0
    else:
      arr[i] = val
      break

# state = [0] * 3
# for i in range(0, pow(3, 3)):
#   print(state)
#   count_up(state, 3)

debug = False

with open("day7_input.txt", "r") as file:
  sum = 0

  for line in file:
    res, values = line.strip().split(':')
    values = list(map(int, values.strip().split(' ')))
    res = int(res)

    ops = len(values) - 1

    if debug:
      print(res, values)

    state = [0] * ops
    for i in range(0, pow(3, ops)):
      calculation = values[0]

      for bit, current_value in zip(state, values[1::]):
        if bit == 0:
          calculation += current_value
        elif bit == 1:
          calculation *= current_value
        else:
          calculation = int(str(calculation) + str(current_value))
      
      if debug:
        print(calculation)
    
      if calculation == res:
        # print(res)
        sum += calculation
        break;
      
      count_up(state, 3)

print(sum)