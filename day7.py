with open("day7_input.txt", "r") as file:
  sum = 0

  for line in file:
    res, values = line.strip().split(':')
    values = list(map(int, values.strip().split(' ')))
    res = int(res)

    ops = len(values) - 1

    # print(res, values)

    for i in range(0, pow(2, ops)):
      # binary_representation = bin(i)[2::].zfill(ops)
      # print(binary_representation)

      calculation = values[0]

      for j in range(0, ops):
        bit = (i >> (ops - 1 - j)) & 1
        current_value = values[j +1]
        if bit == 0:
          calculation += current_value
        else:
          calculation *= current_value
      
      # print(calculation, res)
    
      if calculation == res:
        # print(res)
        sum += calculation
        break;

print(sum)