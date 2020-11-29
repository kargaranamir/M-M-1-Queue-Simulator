from numpy import random as rnd


class job:
    def __init__(self, job_id, arrive_time, mu, theta, is_exp_drop):
        self.job_id = job_id
        self.is_exp_drop = is_exp_drop
        self.arrive_time = arrive_time
        self.service_time = rnd.exponential(1 / mu)


class event:
    def __init__(self, job_id, event_time, status=0):
        self.job_id = job_id
        self.event_time = event_time
        self.status = status


class system:
    def __init__(self, size):
        self.size = size


class simulator:
    def __init__(self, lambda_, mu, theta, size, is_exp_drop = False):
        self.lambda_ = lambda_
        self.mu = mu
        self.theta = theta
        self.size = size
        self.system = system(self.size)
        self.is_exp_drop = is_exp_drop