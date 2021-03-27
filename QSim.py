from numpy import random as rnd


class job:
    def __init__(self, job_id, arrive_time, mu, theta, is_exp_drop):
        self.job_id = job_id
        self.is_exp_drop = is_exp_drop
        self.arrive_time = arrive_time
        self.service_time = rnd.exponential(1 / mu)
        self.drop_time = rnd.exponential(theta) if self.is_exp_drop else theta
        self.service_end_time = self.arrive_time + self.service_time
        self.limit_time = self.arrive_time + self.drop_time


class event:
    def __init__(self, job_id, event_time, status=0):
        self.job_id = job_id
        self.event_time = event_time
        self.status = status


class system:
    def __init__(self, size):
        self.size = size
        self.num_exited = 0
        self.num_dropped = 0
        self.num_blocked = 0
        self.priority_queue = []
        self.events_queue = []
        self.all_jobs = []
        self.queue_status = 0

    def add_event(self, the_new_event):
        if the_new_event:
            i = 0
            j = len(self.events_queue)
            while i < j:
                mid = (i + j) // 2
                if self.events_queue[mid].event_time < the_new_event.event_time:
                    i = mid + 1
                else:
                    j = mid
            self.events_queue.insert(i, the_new_event)

    def add_job(self, the_new_job):
        self.all_jobs.append(the_new_job)
        the_new_event = self.handle_events(the_new_job)
        self.add_event(the_new_event)

    def handle_events(self, the_job, event_time=0, status=0):
        if status == 0:
            self.queue_status = len(self.priority_queue)
            if self.queue_status == self.size:
                self.num_blocked += 1
                return False
            else:
                self.priority_queue.append(the_job)
                return event(the_job.job_id, the_job.service_end_time if self.queue_status == 0 else the_job.limit_time, 2 if self.queue_status == 0 else 1)

        elif status == 1:
            self.num_dropped += 1
            self.priority_queue = [x for x in self.priority_queue if x.job_id != the_job.job_id]
            self.events_queue = [x for x in self.events_queue if x.job_id != the_job.job_id]
            return False

        else:
            self.num_exited += 1
            self.priority_queue = [x for x in self.priority_queue if x.job_id != the_job.job_id]
            self.events_queue = [x for x in self.events_queue if x.job_id != the_job.job_id]
            if len(self.priority_queue) == 0:
                return False
            else:
                self.events_queue = [x for x in self.events_queue if x.job_id != self.priority_queue[0].job_id]
                return event(self.priority_queue[0].job_id, event_time + self.priority_queue[0].service_time, 2)

    def handle_jobs(self):
        the_event, self.events_queue = self.events_queue[0], self.events_queue[1:]
        the_new_event = self.handle_events(self.all_jobs[the_event.job_id], the_event.event_time, the_event.status)
        self.add_event(the_new_event)


class simulator:
    def __init__(self, lambda_, mu, theta, size, is_exp_drop = False):
        self.lambda_ = lambda_
        self.mu = mu
        self.theta = theta
        self.size = size
        self.system = system(self.size)
        self.is_exp_drop = is_exp_drop

    def run(self, num_customers):
        current_time = 0
        job_id = 0
        while job_id < num_customers:
            if len(self.system.events_queue) == 0 or  current_time < self.system.events_queue[0].event_time:
                new_job = job(job_id, current_time, self.mu, self.theta, self.is_exp_drop)
                self.system.add_job(new_job)
                current_time += rnd.exponential(1 / self.lambda_)
                job_id += 1
            else:
                self.system.handle_jobs()
        return self.system.num_blocked / num_customers, self.system.num_dropped / num_customers
