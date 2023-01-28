import time
import tkinter as tk
import numpy as np
from constants import *
import logging as log
import sun_path
from get_coords import get_coords_panel, get_coords_sun
from panel import SolarPanel

## stuff
origin:   int     = 400
distance: int     = 200

def create_animation_window():
  Window = tk.Tk()
  Window.title("Solar panel follows sun")
  Window.geometry(f'{Window_Width}x{Window_Height}')
  return Window

def create_animation_canvas(Window):
  canvas = tk.Canvas(Window)
  canvas.configure(bg="White")
  canvas.pack(fill="both", expand=True)
  return canvas

def main(Window, canvas):

  # Simulation time
  simTime = tk.Label()
  simTime.place(x=50, y=80)

  # Motor param 
  simVolt = tk.Label()
  simVolt.place(x=50, y=100) 
  simAmps = tk.Label()
  simAmps.place(x=50, y=120)

  # create canvas objects
  sun = canvas.create_oval(
    400-radius[0],
    400-radius[0],
    400+radius[0],
    400+radius[0],
    fill="Yellow", outline="Black", width=2)
  
  solar_panel = canvas.create_oval(
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

  # Initializations
  t: float = 0.0      
  panel = SolarPanel() 
  (xPanel, yPanel) = get_coords_panel(canvas, solar_panel)
  sun_ = sun_path.Sun(distance, xPanel, yPanel)
  coordX = 600 # arrow endpoint
  coordY = 600 # arrow endpoint

  # main loop
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

    # Update time label
    t += dt
    simTime.configure(text=f"Simulation time: {str(round(t,5))} sec")

    # Update motor param label
    simVolt.configure(text=f"Motor voltage: {str(round(log.m_voltage,5))} V")
    simAmps.configure(text=f"Motor current: {str(round(log.m_current,5))} A")
  
    # Update GUI
    Window.update()
    time.sleep(dt)


if __name__ == "__main__":
  # Create and call GUI window
  Animation_Window = create_animation_window()
  Animation_canvas = create_animation_canvas(Animation_Window)
  main(Animation_Window, Animation_canvas)