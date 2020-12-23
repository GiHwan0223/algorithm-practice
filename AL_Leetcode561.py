def minSum(nums) -> int:
  # define variables of result
  result = 0
  # Sort numbers to compare numbers sequentialy
  nums.sort()

  # Compare two numbers
  for i,n in enumerate(nums):
    # sum of even cases
    if i % 2 == 0:
      result = result + n
  return result


nums = [1,4,3,2]
print(minSum(nums))

nums = [1,4,8,3,2,5,7,6,9]
print(minSum(nums))
