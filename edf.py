from queue import Queue

def is_schedulable(events):
    utilization = 0
    for i in range(len(events)):
        event = events[i]
        duration = event.duration
        period = event.period
        utilization += (duration/period)

    if utilization >= 1:
        print("Can't handle orders today")


def earliest_deadline_first(events, end_time):
    is_schedulable(events) 
        
    out_str = ""
    event_deadlines_in_lcm = []
    q = Queue(maxsize=end_time)

    for i in range(len(events)):
        event = events[i]
        get_deadlines_in_lcm(event, end_time, event_deadlines_in_lcm)  

    event_deadlines_in_lcm.sort(key = lambda x: x[1])
    # print(event_deadlines_in_lcm)
    for event_deadline in event_deadlines_in_lcm:
        # print(event_deadline)
        q.put(event_deadline)

    event = None 
    deadline = None
    lock = True

    idle = 0
    for time in range(end_time):
        if lock == True:
            if q.empty():
                idle += 1
                print(str(time) + ' ' + "Idle")
                out_str += (str(time) + ' ' + "Idle")
                out_str += '\n'
                continue
            event, deadline = q.get()
            
            if event is  None:
                idle += 1
                print(str(time) + ' ' + "Idle")
                out_str += (str(time) + ' ' + "Idle")
                out_str += '\n'
                    
            else:
                
                duration = event.duration
                lock = False
         
        if time + duration > deadline:
            print(event.name + ' deadline missed')
            out_str += (event.name + ' deadline missed')
            out_str += '\n'
            pass
        else:
            duration-= 1 
            if duration == 0:
                lock = True
                event.waiting_time += ((time+1 - event.arrival_time) - event.duration)
                event.arrival_time += event.period

            print(str(time) + ' ' + event.name)
            out_str += (str(time) + ' ' + event.name)
            out_str += '\n'

    print('Idle time = ' + str(idle))
    out_str += ('Idle time = ' + str(idle))
    out_str += '\n'
    
    for event in events:
        print(event.name +  ' waiting time = ' + str(event.waiting_time))
        out_str += (event.name +  ' waiting time = ' + str(event.waiting_time))
        out_str += '\n'

    
    output_file = open("out-edf.txt", "w")
    output_file.writelines(out_str)
    output_file.close()

    return None

def get_deadlines_in_lcm(event, end_time, event_deadlines_in_lcm):

    deadline = event.deadline
    period = event.period
    # print(deadline)
    # print(period)
    for time in range(0, end_time):
        if time % period == 0:
            event_deadlines_in_lcm.append((event, time + deadline))

    return None