import math

def is_good(nums):
  for i in range(0, len(nums)):
    current = nums[i]
    before = nums[0:i:]
    after = nums[i+1::]

    # print("Current:", current, constraints[current])
    # print(nums, "Before:", before, "After: ", after)

    for nb in before:
      if nb in (constraints[current])["before"]:
        # print("number(" + str(nb) + ") before is in after")
        return (False, current, nb)

    for na in after:
      if na in (constraints[current])["after"]:
        # print("number(" + str(na) + ") after is in before")
        return (False, current, na)
  return (True, )

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

    res = is_good(nums)
    good = res[0]

    if good:
      # mid = nums[math.floor(len(nums) / 2)]
      # print(mid)
      # sum += mid
      pass
    else:
      good = False
      while not good:
        x1 = res[1]
        x2 = res[2]

        # print("Conflict", x1, x2)

        i1 = nums.index(x1)
        i2 = nums.index(x2)
        nums[i1], nums[i2] = nums[i2], nums[i1]

        res = is_good(nums)
        good = res[0]
      
      # print("Solved conflict:", nums)
      mid = nums[math.floor(len(nums) / 2)]
      # print(mid)
      sum += mid


      pass


    # break;
  
  print(sum)
