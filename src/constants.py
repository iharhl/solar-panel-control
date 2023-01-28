import math

PI = math.pi

# Radius for canvas objects
radiusSun:    int         = 30
radiusPanel:  int         = 15
radius:       list[int]   = [radiusSun, radiusPanel]

# Time step [s]
dt: float = 0.00001

# Window dimensions
Window_Width:   int = 800
Window_Height:  int = 800

# Controller gains
Kp: int = 240 * 10
Ki: int = 180 * 10

# Motor parameters
L: float = 1e-5         # Inductance, [H]
V: float = 1.0          # Voltage, [V]
R: float = 1.0          # Resistance, [Ohm]
Kg: float = 2000.0      # Gear ratio, []
Kf: float = 0.07        # Back EMF cosntant, [V/(rad/s)]
Kt: float = 0.07        # Torque constant, [N*m/A]

# Panel parameters
J: float = 8.6108       # Inertia, [kg*m^2]
Kd: float = 5.0         # Damping constant [N*m/(rad/s)]