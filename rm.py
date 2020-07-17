from queue import Queue
from queue import PriorityQueue
import heapq

def is_schedulable(events):
    n = len(events)
    u = n * (2 ** (1/n) - 1)
    temp = 0
    for i in range(n):
        event = events[i]
        temp += (event.duration / event.period)
    
    if temp <= u:
        return True
    else:
        return False

def rate_monotonic(events, end_time):

    if is_schedulable(events) is False:
        print("Can't handle orders today")
    
    idle = 0
    q = PriorityQueue(maxsize=end_time)

    out_str = ""
    for time in range(end_time):
        for i in range(len(events)):
            event = events[i]
            if time % event.period == 0:
                event.arrival_time = time
                event.current_duration = event.duration
                event.current_deadline = event.arrival_time + event.deadline
                
                q.put((event.period, event))
        if q.empty():
            idle += 1
            print(str(time) + ' ' + 'Idle')
            out_str += (str(time) + ' ' + "Idle")
            out_str += '\n'
        else:
            event_period, event = q.queue[0]

            if event is not None:
                remaining = event.current_duration - 1
                event.current_duration -= 1
                if remaining == 0:
                    event.waiting_time += ((time+1 - event.arrival_time) - event.duration)
                    q.get()
                    if time + event.current_duration > event.current_deadline:
                       
                        print(str(time) + ' ' + event.name + ' deadline missed')
                        out_str += (event.name + ' deadline missed')
                        out_str += '\n'
                        out_str += (str(time) + ' ' + event.name)
                        out_str += '\n'
                    else:
                        print(str(time) + ' ' + event.name)
                        out_str += (str(time) + ' ' + event.name)
                        out_str += '\n'
                else:
                    print(str(time) + ' ' + event.name)
                    out_str += (str(time) + ' ' + event.name)
                    out_str += '\n'
            else:
                idle += 1
                print('Idle time = ' + str(idle))
                out_str += (str(time) + ' ' + "Idle")
                out_str += '\n'
    
    print('Idle time = ' + str(idle))
    out_str += ('Idle time = ' + str(idle))
    out_str += '\n'

    for event in events:
        print(event.name +  ' waiting time = ' + str(event.waiting_time))
        out_str += (event.name +  ' waiting time = ' + str(event.waiting_time))
        out_str += '\n'
    

    output_file = open("out-rm.txt", "w")
    output_file.writelines(out_str)
    output_file.close()
    return None
#     event_periods_in_lcm = []
#     q = Queue(maxsize=end_time)

#     for i in range(len(events)):
#         event = events[i]
#         get_periods_in_lcm(event, end_time, event_periods_in_lcm)  

#     event_periods_in_lcm.sort(key = lambda x: x[2])

#     for i in range(1, len(event_periods_in_lcm)):
#         if event_periods_in_lcm[i-1][2] == event_periods_in_lcm[i][2]:
#             if event_periods_in_lcm[i-1][0].period > event_periods_in_lcm[i][0].period:
#                 temp = event_periods_in_lcm[i]
#                 event_periods_in_lcm[i] = event_periods_in_lcm[i-1]
#                 event_periods_in_lcm[i-1] = temp
            

#     print(len(event_periods_in_lcm))
#     for i in range(len(event_periods_in_lcm)):
#         print(event_periods_in_lcm[i])

#     process_priority_queue = []
#     heapq.heapify(process_priority_queue)
#     temp = []
#     for i in range(len(event_periods_in_lcm)):
#         if event_periods_in_lcm[i][2] == 0:
#             process_priority_queue.append(event_periods_in_lcm[i][2], (event_periods_in_lcm[i][0], event_periods_in_lcm[i][1]))
#     heapq.heapify(process_priority_queue)
#     print(list(process_priority_queue))

    
#     is_lock = False
#     idle = 0
#     event = deadline = arrival_time = None
#     for time in range(end_time):
#         for i in range(len(event_periods_in_lcm)):
#             if time == event_periods_in_lcm[i][2]:
#                 heapq.heappush(process_priority_queue, (event_periods_in_lcm[i][2], event_periods_in_lcm[i][1], event_periods_in_lcm[i][0] ))
                
#                 is_lock = False
        
#         if is_lock == False:
#             arrival_time , deadline, event = heapq.heappop(process_priority_queue)
#             is_lock = True
#             event.current_duration = event.duration

#             event.current_duration -= 1
            
#             if event.current_duration == 0:
#                 event.waiting_time += ((time+1 - arrival_time) - event.duration)
#                 event.current_duration = event.duration
#                 is_lock = False
                
#             print(str(time) + ' ' + event.name)
    
#         else:
#             if time + event.current_duration > deadline:
#                 print(event.name + ' deadline missed')
#             else:
#                 event.current_duration -= 1
#                 if event.current_duration == 0:
#                     event.waiting_time += ((time+1 - arrival_time) - event.duration)
#                     event.current_duration = event.duration
#                     is_lock = False
                
#                 print(str(time) + ' ' + event.name)      
#     return None    


# def get_periods_in_lcm(event, end_time, event_periods_in_lcm):
    
#     deadline = event.deadline
#     period = event.period
#     for time in range(0, end_time):
#         if time % period == 0:
#             event_periods_in_lcm.append((event, time + deadline, time))

#     return None