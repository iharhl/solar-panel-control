import time
import tkinter as tk
import numpy as np

from constants import *
import sun_path
from get_coords import get_coords_panel, get_coords_sun
from panel import SolarPanel

# Initialization
origin:   int     = 400
distance: int     = 200
t:        float   = 0.0      

def create_animation_window():
  Window = tk.Tk()
  Window.title("Solar panel follows sun")
  Window.geometry(f'{Window_Width}x{Window_Height}')
  return Window

def create_animation_canvas(Window: object):
  canvas = tk.Canvas(Window)
  canvas.configure(bg="White")
  canvas.pack(fill="both", expand=True)
  return canvas

def main(Window: object, canvas: object):

  # create canvas objects
  sun: object = canvas.create_oval(
    400-radius[0],
    400-radius[0],
    400+radius[0],
    400+radius[0],
    fill="Yellow", outline="Black", width=2)
  
  solar_panel: object = canvas.create_oval(
    400-radius[1],
    400-radius[1],
    400+radius[1],
    400+radius[1],
    fill="Black", outline="Black", width=2)

  arrow = canvas.create_line(
        400, 
        400, 
        600, # endpoint
        600, # endpoint
        width=6,
        fill='blue',
        arrow=tk.LAST) 

  # init
  k: int = 0
  panel = SolarPanel() 
  (xPanel, yPanel) = get_coords_panel(canvas, solar_panel)
  sun_ = sun_path.Sun(distance, xPanel, yPanel)
  coordX = 600 # arrow endpoint
  coordY = 600 # arrow endpoint

  while True:

    # get coords of the sun
    (oldX, oldY) = get_coords_sun(canvas, sun)

    # move sun to a new position
    (newX, newY) = sun_.sun_step()
    dx: int = newX - oldX
    dy: int = newY - oldY
    canvas.move(sun, dx, dy)

    # solve and update angle of the panel
    thetaSun = sun_.thetaSun
    theta = panel.derive_angle(thetaSun)
    lenX: float = np.sin(theta) * distance
    lenY: float = np.cos(theta) * distance
    coordX = np.abs(origin - lenX)
    coordY = np.abs(origin - lenY)
    canvas.coords(arrow, origin, origin, coordX, coordY)
  
    # Update GUI
    Window.update()
    time.sleep(dt)

    # Update time
    global t
    t += dt


if __name__ == "__main__":

  # Create and call GUI window
  Animation_Window = create_animation_window()
  Animation_canvas = create_animation_canvas(Animation_Window)
  main(Animation_Window, Animation_canvas)