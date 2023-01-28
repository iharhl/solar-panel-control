import motor
import pi_controller
import constants as c

class SolarPanel:

    def __init__(self):
        self.T: float = 0.0 # torque
        self.theta_dot_dot: float = 0.0
        self.theta_dot: float = 0.0
        self.theta: float = 0.0
        self.panelMotor = motor.Motor() 
        self.piController = pi_controller.PiController()

    def panel_step(self):
        self.theta_dot_dot = 1/c.J * (self.T - c.Kd * self.theta_dot)
        self.theta_dot += self.theta_dot_dot * c.dt
        self.theta += self.theta_dot * c.dt

    def derive_angle(self, thetaSun: float) -> float:
        ## TODO correct the mis-match between thetas
        thetaSun += c.PI  
        if thetaSun > c.PI * 2:
            thetaSun -= c.PI * 2
        ##
        voltage = self.piController.pi_step(thetaSun - self.theta)
        self.T = self.panelMotor.motor_step(self.theta_dot, voltage)
        self.panel_step()
        return self.theta
