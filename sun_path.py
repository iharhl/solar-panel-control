import numpy as np 

# Generate path for sun
def points_of_circle(r: int, a: int, b: int) -> list[tuple]:
  circular_path: list[tuple] = []
  for angle in range(0, 360, 1):
    x: int = int(r * np.sin(np.radians(angle)) + a)
    y: int = int(r * np.cos(np.radians(angle)) + b)
    circular_path.append((x,y))
  return circular_path