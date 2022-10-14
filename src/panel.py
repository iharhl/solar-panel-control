## Solar panel equation of motion

class SolarPanel:

    def __init__(self, dt: float) -> None:
        self.J: float = 8.6                 # Inertia, [kg*m^2]
        self.T: float = 0.0                 # Torque
        self.i: float = 0.0                 # Current
        self.Kd: float = 5.0                # Damping constant [N*m/(rad/s)]
        ## Initialize angles
        self.theta_dot_dot: float = 0.0
        self.theta_dot: float = 0.0
        self.theta: float = 0.0
        self.dt: float = dt

    def panel_motion(self) -> None:
        self.theta_dot_dot = 1/self.J * (self.T - self.Kd * self.theta_dot)
        self.theta_dot += self.theta_dot_dot * self.dt
        self.theta += self.theta_dot * self.dt

    def derive_angle(self, voltage) -> float:
        from motor import motor_motion
        [self.T, self.i] = motor_motion(self.theta_dot, self.i, self.dt)
        self.panel_motion()
        return self.theta
