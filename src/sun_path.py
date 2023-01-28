import numpy as np 
import constants as c

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
    """ This theta does not match the theta in simulation -> fix"""
    return np.radians(self.anglePath[self.step])

  def generate_path(self):
    _min_angle = 140.0
    _max_angle = 240.0
    _incr_angle = 0.0001
    for angle in np.arange(_min_angle, _max_angle, _incr_angle):
      x: int = int(self.r * np.sin(np.radians(angle)) + self.a)
      y: int = int(self.r * np.cos(np.radians(angle)) + self.b)
      self.circularPath.append((x,y))
      self.anglePath.append(angle)
    ## TODO set step to 180 deg
    self.step = len(self.circularPath)//2

  def sun_step(self):
    self.step += 1
    if self.step >= len(self.circularPath):
      self.step = 0
    return self.circularPath[self.step]
