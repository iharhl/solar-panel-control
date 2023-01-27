import numpy as np 

class Sun:

  def __init__(self, r: int, a: int, b: int):
    self.r: int = r
    self.a: int = a
    self.b: int = b
    self.step: int = 0
    self.anglePath: list[float] = []
    self.circularPath: list[tuple] = []
    self.generate_path()

  @property
  def thetaSun(self): 
    return np.radians(self.anglePath[self.step])

  def generate_path(self):
    for angle in np.arange(0.0, 360.0, 0.01):
      x: int = int(self.r * np.sin(np.radians(angle)) + self.a)
      y: int = int(self.r * np.cos(np.radians(angle)) + self.b)
      self.circularPath.append((x,y))
      self.anglePath.append(angle)

  def sun_step(self):
    self.step += 1
    if self.step > len(self.circularPath):
      self.step = 0
    return self.circularPath[self.step]
