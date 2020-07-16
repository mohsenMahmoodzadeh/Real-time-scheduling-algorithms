import sys

def least_laxity_first(events, end_time):
    
    laxities = []
    for time in range(end_time):
        for i in range(len(events)):
            event = events[i]
            if time % event.period == 0:
                event.arrival_time = time
                event.current_deadline = time + event.deadline 
                event.current_laxity = event.laxity
            else:
                pass
                event.current_laxity = event.current_deadline - time - event.current_duration
                # event.current_laxity = event.current_deadline - event.current_duration
            laxities.append((event, event.current_laxity))

        laxities.sort(key = lambda x: x[1])
        print(laxities)
        

        for i in range(1, len(laxities)):
            event, event_current_laxity = laxities[i]
            event.current_laxity -= 1
            event_current_laxity -= 1
            laxities[i] = (event, event_current_laxity)

        event, event_current_laxity = laxities[0]
        laxities.clear()

        if time + event.current_duration > event.current_deadline:
            print(str(time) + ' ' + event.name + ' deadline missed')
            print()
        else:
            event.current_duration -= 1
            if event.current_duration == 0:
                event.waiting_time += ((time+1 - event.arrival_time) - event.duration)
                if time < event.arrival_time + event.period:
                    pass
                    # event_current_laxity = event.laxity + event.period - time // event.period
                

                # event.arrival_time += event.period
                # event.current_deadline += event.period
                # event.current_laxity = sys.maxsize * 2 + 1 
                #
                # event.current_laxity = event.laxity + event.period - time // event.period
                # event.current_duration = event.duration
                # event.current_laxity = event.current_deadline - event.duration
                #
            print(str(time) + ' ' + event.name)   
            print()
            
                
        
        
    
    
    
    # event_periods_in_lcm = []

    # events_timebar = []

    # for i in range(len(events)):
    #     event = events[i]
    #     events_timebar.append((event, event.laxity))
    #     # get_periods_in_lcm(event, end_time, event_periods_in_lcm)
    # events_timebar.sort(key = lambda x: x[1])
    # q = Queue(maxsize=end_time)
    # for event_laxity in events_timebar:
    #     q.put(event_laxity)

    # for i in range(len(events)):
    #     event = events[i]
    #     get_periods_in_lcm(event, end_time, event_periods_in_lcm) 
    
    # event_periods_in_lcm.sort(key = lambda x: x[2])

    # for i in range(len(event_periods_in_lcm)):
    #     if i == 0:
    #         prev_event_period = event_periods_in_lcm[i]
    #     else:
    #         curr_event_period = event_periods_in_lcm[i]
    #         if event_periods_in_lcm[i-1][2] == event_periods_in_lcm[i][2]:
    #             if event_periods_in_lcm[i-1][0].period > event_periods_in_lcm[i][0].period:
    #                 temp = event_periods_in_lcm[i]
    #                 event_periods_in_lcm[i] = event_periods_in_lcm[i-1]
                    
    #                 event_periods_in_lcm[i-1] = temp
                    
                
    #             # prev_event_period = event_periods_in_lcm[i]
    #         else:
    #             pass
    #             # prev_event_period = event_periods_in_lcm[i]

    # print(len(event_periods_in_lcm))
    # for i in range(len(event_periods_in_lcm)):
    #     print(event_periods_in_lcm[i])

    
# count_repeat_periods = []

# for i in range(len(events)):
#     event = events[i]
#     end_time / eve


def get_periods_in_lcm(event, end_time, event_periods_in_lcm):
    deadline = event.deadline
    period = event.period
    for time in range(0, end_time):
        if time % period == 0:
            event_periods_in_lcm.append((event, time + deadline, time))
            

    return None