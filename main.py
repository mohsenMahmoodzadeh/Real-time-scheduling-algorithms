from Event import Event
from utils import lcm
from edf import earliest_deadline_first

f = open('input.txt','r')
orders = f.readlines()
f.close()


food_count = int(orders[0])

events = []
periods = []
for i in range(1, food_count + 1): 
    food_name, cook_duration, deadline, period = [x for x in orders[i].split()]
    event = Event(i, food_name, int(cook_duration), int(deadline), int(period))
    events.append(event)
    periods.append(event.period)


# for i in range(len(orders)): 
#     food_name, cook_duration, deadline, period = [x for x in orders[i].split()]
#     event = Event(i, food_name, int(cook_duration), int(deadline), int(period))
#     events.append(event)
#     periods.append(event.period)

utilization = 0
for i in range(len(events)):
    event = events[i]
    duration = event.duration
    period = event.period
    utilization += (duration/period)

if utilization >= 1:
    print("Can't handle orders today")

time = 0
end_time = lcm(periods)
earliest_deadline_first(events, end_time)
