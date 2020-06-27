from queue import Queue



def earliest_deadline_first(events, end_time):
    # priority = []
    # for i in range(len(events)):
    #     event = events[i]
    #     id = event.id
    #     deadline = event.deadline
    #     priority.append((id, deadline))

    # priority.sort(key = lambda x: x[1])

    event_deadlines_in_lcm = []
    q = Queue(maxsize=end_time)

    for i in range(len(events)):
        event = events[i]
        # id = event.id
        # name = event.name
        # deadline = event.deadline
        # get_deadlines_in_lcm(id, deadline)
        get_deadlines_in_lcm(event, end_time, event_deadlines_in_lcm)  

    event_deadlines_in_lcm.sort(key = lambda x: x[1])
    # print(event_deadlines_in_lcm)
    for event_deadline in event_deadlines_in_lcm:
        q.put(event_deadline)

    event = None 
    deadline = None
    lock = True

    switches = 0
    idle = 0
    for time in range(end_time):
        if lock == True:
            if q.empty():
                idle += 1
                print(str(time + 1) + ' ' + "Idle")
                continue
            event, deadline = q.get()
            
            if event is  None:
                idle += 1
                print(str(time + 1) + ' ' + "Idle")
                # continue    
            else:
                switches += 1
                duration = event.duration
                lock = False
         
        if time + duration > deadline:
            print(event.name + ' deadline missed')
        else:
            # duration = event.duration
            duration-= 1 
            if duration == 0:
                lock = True

            print(str(time + 1) + ' ' + event.name)

    print('Idle times = ' + str(idle))
    print('Switches = ' + str(switches - 1))
    
    return None

def get_deadlines_in_lcm(event, end_time, event_deadlines_in_lcm):
    # name = event.name
    
    deadline = event.deadline
    period = event.period
    for time in range(0, end_time):
        if time % period == 0:
            event_deadlines_in_lcm.append((event, time + deadline))

    return None