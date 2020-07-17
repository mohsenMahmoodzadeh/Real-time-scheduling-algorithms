class Event:
    def __init__(self, id, name, duration, deadline, period):
        self.id = id
        self.name = name
        self.duration = duration
        self.current_duration = duration
        self.deadline = deadline
        self.current_deadline = deadline
        self.period = period
        self.current_period = period
        self.arrival_time = 0
        self.arrival_time = 0
        self.waiting_time = 0
        self.laxity = (self.deadline + self.arrival_time) - self.current_duration
        self.current_laxity = self.laxity
        self.miss_deadline = False
    
    