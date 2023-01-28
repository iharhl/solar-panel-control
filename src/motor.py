import constants as c
import logging

class Motor:

    def __init__(self):
        self.i:         float = 0.0
        self.i_dot:     float = 0.0
        self.torque:    float = 0.0

    def motor_step(self, theta_dot: float, voltage: float):
        self.i_dot = 1/c.L * (voltage - c.Kg * c.Kf * theta_dot - c.R * self.i)
        self.i += self.i_dot * c.dt
        self.torque = c.Kg * c.Kt * self.i
        logging.m_voltage = voltage
        logging.m_current = self.i
        return self.torque
