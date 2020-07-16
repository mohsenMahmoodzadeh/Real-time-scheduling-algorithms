from queue import Queue
import heapq
# def rate_monotonic(events,end_time):
#     laxities = []
#     for time in range(end_time):
#         for i in range(len(events)):
#             event = events[i]
#             if time % event.period == 0:
#                 event.arrival_time = time
#                 event.current_deadline = time + event.deadline 
#                 event.current_period = time + event.period
#             else:
#                 pass
#                 # event.current_period = event.current_deadline - time - event.current_duration
#                 # event.current_laxity = event.current_deadline - event.current_duration
#             laxities.append((event, event.current_period))

#         laxities.sort(key = lambda x: x[1])
#         # print(laxities)
        
#         # for i in range(1, len(laxities)):
#         #     # event, event_current_period = laxities[i]
#         #     if laxities[i][1] == laxities[i-1][1]:
#         #         if laxities[i-1][0].duration > laxities[i][0].duration:
#         #             event_i, event_current_period_i = laxities[i]
#         #             event_i1, event_current_period_i1 = laxities[i-1]
#         #             laxities[i] = (event_i1, event_current_period_i1)
#         #             laxities[i-1] = (event_i, event_current_period_i)
                    
#             # if time % event.period == 0:
#             #     event.arrival_time = time
#             #     event.current_deadline = time + event.deadline 
#             #     event.current_period = time + event.period

#         # for i in range(1, len(laxities)):
#         #     event, event_current_period = laxities[i]
#         #     event.current_period -= 1
#         #     event_current_laxity -= 1
#         #     laxities[i] = (event, event_current_laxity)

#         event, event_current_laxity = laxities[0]
#         laxities.clear()

#         if time + event.current_duration > event.current_deadline:
#             print(str(time) + ' ' + event.name + ' deadline missed')
#             print()
#         else:
#             event.current_duration -= 1
#             if event.current_duration == 0:
#                 event.current_duration = event.duration
#                 event.waiting_time += ((time+1 - event.arrival_time) - event.duration)
#                 if time < event.arrival_time + event.period:
#                     pass
#                     # event_current_laxity = event.laxity + event.period - time // event.period
                

#                 # event.arrival_time += event.period
#                 # event.current_deadline += event.period
#                 # event.current_laxity = sys.maxsize * 2 + 1 
#                 #
#                 # event.current_laxity = event.laxity + event.period - time // event.period
#                 # event.current_duration = event.duration
#                 # event.current_laxity = event.current_deadline - event.duration
#                 #
#             print(str(time) + ' ' + event.name)   
#             print()

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
    
    out_str = ""
    
    event_periods_in_lcm = []
    q = Queue(maxsize=end_time)

    for i in range(len(events)):
        event = events[i]
        get_periods_in_lcm(event, end_time, event_periods_in_lcm)  

    event_periods_in_lcm.sort(key = lambda x: x[2])

    for i in range(1, len(event_periods_in_lcm)):
        if event_periods_in_lcm[i-1][2] == event_periods_in_lcm[i][2]:
            if event_periods_in_lcm[i-1][0].period > event_periods_in_lcm[i][0].period:
                temp = event_periods_in_lcm[i]
                event_periods_in_lcm[i] = event_periods_in_lcm[i-1]
                event_periods_in_lcm[i-1] = temp
            

    print(len(event_periods_in_lcm))
    for i in range(len(event_periods_in_lcm)):
        print(event_periods_in_lcm[i])

    process_priority_queue = []
    heapq.heapify(process_priority_queue)
    temp = []
    for i in range(len(event_periods_in_lcm)):
        if event_periods_in_lcm[i][2] == 0:
            process_priority_queue.append(event_periods_in_lcm[i][2], (event_periods_in_lcm[i][0], event_periods_in_lcm[i][1]))
    heapq.heapify(process_priority_queue)
    print(list(process_priority_queue))

    
    is_lock = False
    idle = 0
    event = deadline = arrival_time = None
    for time in range(end_time):
        for i in range(len(event_periods_in_lcm)):
            if time == event_periods_in_lcm[i][2]:
                heapq.heappush(process_priority_queue, (event_periods_in_lcm[i][2], event_periods_in_lcm[i][1], event_periods_in_lcm[i][0] ))
                
                is_lock = False
        
        if is_lock == False:
            arrival_time , deadline, event = heapq.heappop(process_priority_queue)
            is_lock = True
            event.current_duration = event.duration

            event.current_duration -= 1
            
            if event.current_duration == 0:
                event.waiting_time += ((time+1 - arrival_time) - event.duration)
                event.current_duration = event.duration
                is_lock = False
                
            print(str(time) + ' ' + event.name)
    
        else:
            if time + event.current_duration > deadline:
                print(event.name + ' deadline missed')
            else:
                event.current_duration -= 1
                if event.current_duration == 0:
                    event.waiting_time += ((time+1 - arrival_time) - event.duration)
                    event.current_duration = event.duration
                    is_lock = False
                
                print(str(time) + ' ' + event.name)


            
    return None    
    # return None         
    #     if lock == True:
    #         if q.empty():
    #             idle += 1
    #             print(str(time) + ' ' + "Idle")
    #             out_str += (str(time) + ' ' + "Idle")
    #             out_str += '\n'
    #             continue
    #         event, deadline, arrival_time = q.get()
            
    #         if event is None:
    #             idle += 1
    #             print(str(time) + ' ' + "Idle")
    #             out_str += (str(time) + ' ' + "Idle")
    #             out_str += '\n'
    #             # continue    
    #         else:
    #             duration = event.duration
    #             lock = False
         
    #     if time + duration > deadline:
    #         print(event.name + ' deadline missed')
    #         out_str += (event.name + ' deadline missed')
    #         out_str += '\n'
    #         pass
    #     else:
    #         # duration = event.duration
    #         duration-= 1 
    #         if duration == 0:
    #             lock = True
    #             event.waiting_time += ((time+1 - event.arrival_time) - event.duration)
    #             # event.waiting_time += ((deadline - event.arrival_time) - event.duration)
    #             event.arrival_time += event.period

           
    #         print(str(time) + ' ' + event.name)
    #         out_str += (str(time) + ' ' + event.name)
    #         out_str += '\n'

    # print('Idle time = ' + str(idle))
    # out_str += ('Idle time = ' + str(idle))
    # out_str += '\n'
    
    
    # for event in events:
    #     print(event.name +  ' waiting time = ' + str(event.waiting_time))
    #     out_str += (event.name +  ' waiting time = ' + str(event.waiting_time))
    #     out_str += '\n'


    
    # # output_file = open("out-rms.txt", "w")
    # # output_file.writelines(out_str)
    # # output_file.close()

    # return None

def get_num_entered_events(end_time, event_periods_in_lcm):
    count_enetered_events = []
    for i in range(end_time):
        count_enetered_events.append(0)

    for t in range(end_time):
        if t == event_periods_in_lcm[2]:
            count_enetered_events[t] += 1
    
    return count_enetered_events


def get_periods_in_lcm(event, end_time, event_periods_in_lcm):
    
    deadline = event.deadline
    period = event.period
    for time in range(0, end_time):
        if time % period == 0:
            event_periods_in_lcm.append((event, time + deadline, time))

    return None