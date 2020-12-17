def trap(height):
  # if there is no heught, nothing can be trapped.
  if not height:
    return 0
  
  # Define toal trapped volume
  totalVolume = 0
  # Set left and right walls
  leftWall = 0
  rightWall = len(height)-1
  # Set each wall's max height from the beginning values
  leftWallMax = height[leftWall]
  rightWallMax = height[rightWall]
  # Check a trap while the leftWall meets the rightWall
  while leftWall < rightWall:
    # Find wall's max height using max function
    leftWallMax = max(height[leftWall], leftWallMax)
    rightWallMax = max(height[rightWall], rightWallMax)
    # Get volume by moving walls.
    if leftWallMax <= rightWallMax:
      totalVolume = totalVolume + leftWallMax - height[leftWall]
      leftWall = leftWall + 1
    else:
      totalVolume = totalVolume + rightWallMax - height[rightWall]
      rightWall = rightWall - 1
  return totalVolume

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
height = [4,2,0,3,2,5]
print(trap(height))