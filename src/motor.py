from constants import *

def motor_motion(theta_dot: float = 0.0, i: float = 0.0) -> list[float]:
    i_dot = 1/L * (V - Kg * Kf * theta_dot - R * i)
    i += i_dot * dt
    torque = Kg * Kt * i
    return [torque, i]
