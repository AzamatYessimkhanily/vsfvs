import math

def countPoints(maxDist, angle1, angle2, points):
  tot = 0
  for (x,y) in points:
    theta = math.atan(y/x)
    dist = math.sqrt(x ** 2 + y ** 2)
    if theta > angle1 and theta < angle2:
      if dist < maxDist:
        tot += 1
  return tot