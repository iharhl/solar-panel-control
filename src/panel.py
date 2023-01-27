import motor
import pi_controller
import constants as c

class SolarPanel:

    def __init__(self):
        self.J: float = 8.6108                  # Inertia, [kg*m^2]
        self.T: float = 0.0                     # Torque
        self.Kd: float = 5.0                    # Damping constant [N*m/(rad/s)]
        self.theta_dot_dot: float = 0.0
        self.theta_dot: float = 0.0
        self.theta: float = 0.0
        self.panelMotor = motor.Motor() 
        self.piController = pi_controller.PiController()

    def panel_step(self):
        self.theta_dot_dot = 1/self.J * (self.T - self.Kd * self.theta_dot)
        self.theta_dot += self.theta_dot_dot * c.dt
        self.theta += self.theta_dot * c.dt

    def derive_angle(self, thetaSun: float) -> float:
        voltage = self.piController.pi_step(thetaSun - self.theta)
        self.T = self.panelMotor.motor_step(self.theta_dot, voltage)
        self.panel_step()
        return self.theta
