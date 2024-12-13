import math


with open("day5_input.txt", "r") as file:
  rules, updates = file.read().split("\n\n")

  constraints = [{"after": set(), "before": set()} for _ in range(100)]

  for rule in rules.split():
    nums = rule.split('|')
    l = int(nums[0])
    r = int(nums[1])

    (constraints[l])["before"].add(r)
    (constraints[r])["after"].add(l)

  sum = 0
  for update in updates.split():
    nums = list(map(int, update.split(',')))

    is_good = True
    for i in range(0, len(nums)):
      current = nums[i]
      before = nums[0:i:]
      after = nums[i+1::]

      # print("Current:", current, constraints[current])
      # print(nums, "Before:", before, "After: ", after)

      for nb in before:
        if nb in (constraints[current])["before"]:
          # print("number(" + str(nb) + ") before is in after")
          is_good = False
          break;

      for na in after:
        if na in (constraints[current])["after"]:
          # print("number(" + str(na) + ") after is in before")
          is_good = False
          break;


    
    if is_good:
      mid = nums[math.floor(len(nums) / 2)]
      print(mid)
      sum += mid

    # break;
  
  print(sum)

# 4609