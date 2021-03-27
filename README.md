# M-M-1-Queue-Simulator
#### _M/M/1/K queue Python3 simulator_
A M/M/1/K queue Python3 simulator that compares the simulation results (QSim.py module) against the analytics results (QAnalyic.py module).
The queue have limited capacity K and processes may be blocked (if queue is full) or leave queue before get service (there is a deadline for each process) or get service from server.

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Features

- Compute probability of process blocking or leaving in a limited queue in analytic and simulation ways

## How to use

```sh
import QAnalytic
import QSim

if __name__ == "__main__":
# set parameters
    mu = 1 # service rate
    theta = 2 # deadline rate or deadline time
    lambdas = 5 # arrival rate of customers
    num_customers = 10 ** 6 #number of customers in simulation 
    queue_size = 12 #size of queue
    is_exp_drop = True # or False
    
    simulator = QSim.simulator(lambda_,
                                mu,
                                theta,
                                queue_size,
                                is_exp_drop)

    analyzer = QAnalytic.analyzer(lambda_,
                                  mu,
                                  theta,
                                  queue_size,
                                  is_exp_drop)

            sim_pb, sim_pd = simulator.run(num_customers)
            anal_pb, anal_pd = analyzer.run()
            print(f"is_exp_drop:{is_exp_drop}, lambda:{lambda_}, mu:{mu}, theta:{theta} => simulation pb:{sim_pb}, analytic pb:{anal_pb}, simulation pd:{sim_pd}, analytic pd:{anal_pd} \n")
```

## Parameters

| QSim and QAnalytic |
| ------------- |
| lambda_ : arrival rate of customers      |
| mu: server rate       |
| theta: deadline rate or deadline time     | 
| size: size of the Queue (K) |
| is_exp_drop: Is deadline time follow a exponential distribution? or not (Fixed)?       |
| num_customers: number of customers | 
## License

GNU General Public License v3.0