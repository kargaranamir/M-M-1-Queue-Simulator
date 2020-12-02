# M-M-1-Queue-Simulator
A M/M/1/K queue Python3 simulator that compares the simulation results (QSim.py module) against the analytics results (QAnalyic.py module).
The queue have limited capacity K and processes may be blocked (if queue is full) or leave queue before get service (there is a deadline for each process) or get service from server.



## Parameters

| QSim and QAnalytic |
| ------------- |
| lambda_ : arrival rate of customers      |
| mu: server rate       |
| theta: deadline rate or deadline time     | 
| size: size of the Queue (K) |
| is_exp_drop: Is deadline time follow a exponential distribution? or not (Fixed)?       |
| num_customers: number of customers | 