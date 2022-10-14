from constants import *

def control(error: float, error_prev: float) -> float:
    output: float = error * Kp + (error_prev + error * dt) * Ki
    return output