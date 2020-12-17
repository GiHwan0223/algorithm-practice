def threeSum1(nums):
  # Define variables.
  result = []
  # Sort a list first to handle
  nums.sort()

  # Get each number.
  for i in range(0, len(nums)-2):
    # skip duplicated cases
    if i > 0 and nums[i] == nums[i-1]:
      continue
    for j in range(i+1, len(nums)-1):
      # skip duplicated cases
      if j > i+1 and nums[j] == nums[j-1]:
        continue
      for k in range(j+1, len(nums)):
        # skip duplicated cases
        if k > j+1 and nums[k] == nums[k-1]:
          continue
        # Get a result
        if nums[i] + nums[j] + nums[k] == 0:
          result.append((nums[i],nums[j],nums[k]))

  return result

def threeSum(nums):
  # define result list variable
  result = []
  # sort a list
  nums.sort()

  # sum should be 0 so, if the fist list value is bigger than result that already sum two values
  for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
      continue
    left = i + 1
    right = len(nums) -1
    #shrink scope while sum values
    while left < right:
      sum = nums[i] + nums[left] + nums[right]
      if sum < 0:
        left = left + 1
      elif sum > 0:
        right = right -1
      else:
        result.append((nums[i],nums[left],nums[right]))

        while left < right and nums[left] == nums[left+1]:
          left = left + 1
        while left < right and nums[right] == nums[right-1]:
          right = right -1
        left = left + 1
        right = right - 1
  return result




nums = [1,-1,-1,0]

print(threeSum(nums))