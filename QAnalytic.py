import numpy as np
from functools import reduce
import operator


class analyzer:
    def __init__(self, lambda_, mu, theta, size, is_exp_drop = False):
        self.lambda_ = lambda_
        self.mu = mu
        self.theta = theta
        self.size = size
        self.is_exp = is_exp_drop
        self.coefficients = []
        self.pb = 0
        self.pd = 0
        self.p0 = 0

