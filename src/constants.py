
# Radius for canvas objects
radiusSun:    int         = 30
radiusPanel:  int         = 15
radius:       list[int]   = [radiusSun, radiusPanel]

# Time step [s]
dt: float = 0.02 

# Window dimensions
Window_Width:   int = 800
Window_Height:  int = 800

# Controller gains
Kp: int = 240
Ki: int = 180

# Motor parameters
L: float = 1e-5         # Inductance, [H]
V: float = 1.0          # Voltage, [V]
R: float = 1.0          # Resistance, [Ohm]
Kg: float = 2000.0      # Gear ratio, []
Kf: float = 0.07        # Back EMF cosntant, [V/(rad/s)]
Kt: float = 0.07        # Torque constant, [N*m/A]