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

    def phi(self, n):
        if self.is_exp:
            return np.math.factorial(n) / reduce(operator.mul, [(self.mu + (i / self.theta)) for i in range(0, n + 1)], 1)
        else:
            return (np.math.factorial(n)/(self.mu ** (n + 1))) \
                   * (1 - (np.exp(-1 * self.mu * self.theta)) * sum([(((self.mu * self.theta) ** i)/np.math.factorial(i)) for i in range(0, n)]))

    def run(self):
        for i in range(0,self.size+1):
            if i == 0:
                the_coef = 1
            elif i == 1:
                the_coef = self.lambda_ / self.mu
            else:
                the_coef = ((self.lambda_ ** i) * self.phi(i - 1)) / np.math.factorial(i - 1)
            self.coefficients.append(the_coef)

        self.p0 = 1/sum(self.coefficients)
        self.pb = self.p0 * self.coefficients[-1]
        self.pd = (1 - (self.mu / self.lambda_) * (1 - self.p0)) - self.pb
        return self.pb, self.pd