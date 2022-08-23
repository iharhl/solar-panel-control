## Motor model

L: float = 1e-5         # Inductance, [H]
V: float = 1.0          # Voltage, [V]
R: float = 1.0          # Resistance, [Ohm]
Kg: float = 2000.0      # Gear ratio, []
Kf: float = 0.07        # Back EMF cosntant, [V/(rad/s)]
Kt: float = 0.07        # Torque constant, [N*m/A]

def motor_motion(theta_dot: float = 0.0, i: float = 0.0, dt: float = 0.02) -> list[float]:
    i_dot = 1/L * (V - Kg * Kf * theta_dot - R * i)
    i += i_dot * dt
    torque = Kg * Kt * i
    return [torque, i]
