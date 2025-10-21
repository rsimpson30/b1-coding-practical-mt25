class Controller:
    '''A controller implementing PD feedback.'''
    def __init__(self, proportional_gain : float, derivative_gain : float):
        self.k_p = proportional_gain
        self.k_d = derivative_gain

    def get_action(self, cur_error, prev_error = 0):
        # Return control action for this timestep
        action = self.k_p * cur_error + self.k_d * (cur_error - prev_error)
        return action