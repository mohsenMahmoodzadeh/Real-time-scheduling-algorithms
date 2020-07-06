class Event:
    def __init__(self, id, name, duration, deadline, period, arrival_time=0, waiting_time=0):
        self.id = id
        self.name = name
        self.duration = duration
        self.deadline = deadline
        self.period = period
        self.arrival_time = arrival_time
        self.waiting_time = waiting_time
    
    