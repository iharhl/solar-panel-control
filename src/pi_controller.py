import constants as c
    
class PiController:

    def __init__(self):
        self.P_term:    float = 0.0
        self.I_term:    float = 0.0
        self.command:   float = 0.0

    def pi_step(self, err: float):
        self.P_term = c.Kp * err
        self.I_term  += c.Ki * err * c.dt
        self.command = self.P_term + self.I_term
        return self.command
