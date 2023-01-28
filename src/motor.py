import constants as c
import logging

class Motor:

    def __init__(self):
        self.i:         float = 0.0
        self.i_dot:     float = 0.0
        self.torque:    float = 0.0

    # def motor_step(self, theta_dot: float, voltage: float):
    #     self.i_dot = 1/c.L * (voltage - c.Kg * c.Kf * theta_dot - c.R * self.i)
    #     self.i += self.i_dot * c.dt
    #     self.torque = c.Kg * c.Kt * self.i
    #     return self.torque

    def motor_step(self, theta_dot: float, voltage: float):

        # Runge-Kutta method (4th order)
        iTemp = self.i
        k1 = 1/c.L * (voltage - c.Kg * c.Kf * theta_dot - c.R * iTemp)
        iTemp = self.i + c.dt*k1/2
        k2 = 1/c.L * (voltage - c.Kg * c.Kf * theta_dot - c.R * iTemp)
        iTemp = self.i + c.dt*k2/2
        k3 = 1/c.L * (voltage - c.Kg * c.Kf * theta_dot - c.R * iTemp)
        iTemp = self.i + c.dt*k3
        k4 = 1/c.L * (voltage - c.Kg * c.Kf * theta_dot - c.R * iTemp)
        self.i += c.dt * (k1 + 2*k2 + 2*k3 + k4)/6

        self.torque = c.Kg * c.Kt * self.i

        logging.m_voltage = voltage
        logging.m_current = self.i

        return self.torque
