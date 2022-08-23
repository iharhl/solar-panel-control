## PI controller to control panel voltage to follow the sun

Kp: int = 240
Ki: int = 180

def controller(error: float, error_prev: float, dt: float = 0.02) -> float:
    output: float = error * Kp + (error_prev + error * dt) * Ki
    return output