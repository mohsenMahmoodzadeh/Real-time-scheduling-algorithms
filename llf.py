from queue import PriorityQueue
def least_laxity_first(events, end_time):
    
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
                event.miss_deadline = False
                q.put((event.laxity, event.name, event))
            event.current_laxity = (event.current_deadline + event.arrival_time) - time -  event.current_duration
        
        temp_q = PriorityQueue(maxsize = end_time)
        while not q.empty():
            # temp_q.put(q.queue[0])
            event_laxity, event_name, event = q.get()
            temp_q.put((event_laxity, event_name, event))
            # temp_q.put(q.get())
        
        q = temp_q

        if not q.empty():
            event_laxity, event_name, event = q.queue[0]
        else:
            idle += 1
            print('Idle time = ' + str(idle))
            out_str += (str(time) + ' ' + "Idle")
            out_str += '\n'
            
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
                if event.current_laxity < 0 and  event.miss_deadline is False:
                    event.miss_deadline = True
                    print(str(time) + ' ' + event.name + ' will miss deadline')
                    out_str += (str(time) + ' ' + event.name + ' will miss deadline')
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





        # if q.empty():
        #     idle += 1
        #     print(str(time) + ' ' + 'Idle')
        #     out_str += (str(time) + ' ' + "Idle")
        #     out_str += '\n'
        # else:
        #     event_period, event = q.queue[0]

        #     if event is not None:
        #         remaining = event.current_duration - 1
        #         event.current_duration -= 1
        #         if remaining == 0:
        #             event.waiting_time += ((time+1 - event.arrival_time) - event.duration)
        #             q.get()
        #             if time + event.current_duration > event.current_deadline:
                       
        #                 print(str(time) + ' ' + event.name + ' deadline missed')
        #                 out_str += (event.name + ' deadline missed')
        #                 out_str += '\n'
        #                 out_str += (str(time) + ' ' + event.name)
        #                 out_str += '\n'
        #             else:
        #                 print(str(time) + ' ' + event.name)
        #                 out_str += (str(time) + ' ' + event.name)
        #                 out_str += '\n'
        #         else:
        #             print(str(time) + ' ' + event.name)
        #             out_str += (str(time) + ' ' + event.name)
        #             out_str += '\n'
        #     else:
        #         idle += 1
        #         print('Idle time = ' + str(idle))
        #         out_str += (str(time) + ' ' + "Idle")
        #         out_str += '\n'
    
    print('Idle time = ' + str(idle))
    out_str += ('Idle time = ' + str(idle))
    out_str += '\n'

    for event in events:
        print(event.name +  ' waiting time = ' + str(event.waiting_time))
        out_str += (event.name +  ' waiting time = ' + str(event.waiting_time))
        out_str += '\n'
    

    # output_file = open("out-llf.txt", "w")
    # output_file.writelines(out_str)
    # output_file.close()

    return None


    # laxities = []
    # for time in range(end_time):
    #     for i in range(len(events)):
    #         event = events[i]
    #         if time % event.period == 0:
    #             event.arrival_time = time
    #             event.current_deadline = time + event.deadline 
    #             event.current_laxity = event.laxity
    #         else:
    #             pass
    #             event.current_laxity = event.current_deadline - time - event.current_duration
    #         laxities.append((event, event.current_laxity))

    #     laxities.sort(key = lambda x: x[1])
    #     # print(laxities)
        
    #     for i in range(1, len(laxities)):
    #         event, event_current_laxity = laxities[i]
    #         event.current_laxity -= 1
    #         event_current_laxity -= 1
    #         laxities[i] = (event, event_current_laxity)

    #     event, event_current_laxity = laxities[0]
    #     laxities.clear()

    #     if time + event.current_duration > event.current_deadline:
    #         print(str(time) + ' ' + event.name + ' deadline missed')
    #     else:
    #         event.current_duration -= 1
    #         if event.current_duration == 0:
    #             event.waiting_time += ((time+1 - event.arrival_time) - event.duration)
    #             # event.arrival_time += event.period
    #             # event.current_deadline += event.period
    #             # event.current_duration = event.duration
    #             # event.current_laxity = event.current_deadline - event.duration
                
    #         print(str(time) + ' ' + event.name)