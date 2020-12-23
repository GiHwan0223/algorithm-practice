def multipleExcelptMe(nums):
  length = len(nums)
  result = []

  for i in range(0,length):
    multiple = 1
    if i ==0:
      for index in range(i+1,length):
        multiple = multiple * nums[index]
      result.append(multiple)
    elif i > 0 and i < length-1:
      for index in range(0,i):
        multiple = multiple * nums[index]
      for index in range(i+1,length):
        multiple = multiple * nums[index]
      result.append(multiple)
    else:
      for index in range(0, length-1):
        multiple = multiple * nums[index]
      result.append(multiple)
  return result

def multipleExcelptMe2(nums):
  result = []
  multiple = 1

  # Multiple left side
  for i in range(0, len(nums)):
    result.append(multiple)
    multiple = multiple * nums[i]
  multiple = 1
  # Multiple right side (append)
  for i in range(len(nums)-1, 0-1, -1):
    result[i] = result[i] * multiple
    multiple = multiple * nums[i]
  return result



nums = [1,2,3,4,5]

print(multipleExcelptMe2(nums))

nums = [2,3,4,5]

print(multipleExcelptMe2(nums))