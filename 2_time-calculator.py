def add_time(start, duration, weekday=False):

    # create variables for code

    # a variable for start argument
    find_position1 = start.find(':')
    hour = start[:find_position1]
    minute = start[find_position1+1:find_position1+4]

    # a variable for duration argument
    find_position2 = duration.find(':')
    add_hour = duration[:find_position2]
    add_minute = duration[find_position2+1:]


    # calculate the hour and the minute to print the results
    result_hour =int(hour) + int(add_hour)
    result_minute=str(int(minute) + int(add_minute))


    # use this variable when the time pasees more than two days
    time=''
    day_result=''
    day_number=1


    # only when weekday is True, use this list
    weekday_list = ['Monday','tuesday','Wednesday','Thursday','Friday','saturDay','Sunday']



    # make weekday position variable to calculate later

    if weekday == False:
        weekday_position = 0

    else:
        weekday_position = weekday_list.index(weekday)


    # add 1 hour when the minute is more than 60

    if int(result_minute) >=60:
        result_minute = str(int(result_minute) -60)
        result_hour +=1

        if int(result_minute) < 10:
            result_minute = '0' + result_minute


    elif int(result_minute) < 10:
        result_minute = '0' + result_minute

    else:
        pass
        
    # create weekday_calculation function and calculate total time and weekday

    final_weekday_position = 0

    def weekday_calculation(num):
        if num <7:
            pass

        elif num == 7:
            num = 0

        else:
            for i in range(8, num+2, 7):
                num -=7

        return num

    #AM calculation

    if 'AM' in start:
        if result_hour<48:

            if result_hour in range(0,12):
                time='AM'

            elif result_hour in range(12,24):

                if result_hour == 12:
                    time='PM'

                elif result_hour >12:
                    result_hour -=12
                    time='PM'

                else:
                    pass

            elif result_hour in range(24,48):
                if result_hour<36:
                    time='AM'
                    result_hour -=24
                    day_result=' (next day)'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)

                elif result_hour ==36:
                    time='PM'
                    result_hour -=24
                    day_result=' (next day)'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)

                elif result_hour > 36:
                    time='PM'
                    result_hour -=36
                    day_result=' (next day)'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)

                else:
                    pass

        else:
            for i in range(48,int(add_hour)+int(hour),24):
                day_number +=1
                result_hour -=24
                weekday_position +=1

            weekday_position +=1
            result_hour -=24

            if result_hour in range(0,12):
                time='AM'
                day_result=' (' + str(day_number) + ' days later' + ')'
                final_weekday_position = weekday_calculation(weekday_position)


            elif result_hour in range(12,24):

                if result_hour == 12:
                    time='PM'
                    day_result=' (' + str(day_number) + ' days later' + ')'
                    final_weekday_position = weekday_calculation(weekday_position)

                elif result_hour >12:
                    result_hour -=12
                    time='PM'
                    day_result=' (' + str(day_number) + ' days later' + ')'
                    final_weekday_position = weekday_calculation(weekday_position)

                else:
                    pass

            elif result_hour in range(24,48):
                if result_hour<36:
                    time='AM'
                    result_hour -=24
                    day_result=' (' + str(day_number+1) + ' days later' + ')'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)

                elif result_hour ==36:
                    time='PM'
                    result_hour -=24
                    day_result=' (' + str(day_number+1) + ' days later' + ')'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)

                elif result_hour > 36:
                    time='PM'
                    result_hour -=36
                    day_result=' (' + str(day_number+1) + ' days later' + ')'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)


                else:
                    pass

    #PM calculation
    elif 'PM' in start:
        if result_hour<36:
            if result_hour in range(1,12):
                time='PM'

            elif result_hour in range(12,24):
                result_hour -=12
                time='AM'
                day_result=' (next day)'
                weekday_position +=1
                final_weekday_position = weekday_calculation(weekday_position)

            elif result_hour in range(24,36):
                if result_hour ==24:
                    result_hour -=12
                    time='PM'
                    day_result=' (next day)'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)

                elif result_hour >24:
                    result_hour -=24
                    time='PM'
                    day_result=' (next day)'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)

                else:
                    pass
        else:
            for i in range(36,int(add_hour)+int(hour),24):
                day_number +=1
                result_hour -=24
                weekday_position +=1

            weekday_position +=1
            result_hour -=24


            if result_hour in range(1,12):
                time='PM'
                day_result=' (' + str(day_number) + ' days later' + ')'
                final_weekday_position = weekday_calculation(weekday_position)


            elif result_hour ==12:
                time='AM'
                day_result=' (' + str(day_number+1) + ' days later' + ')'
                weekday_position +=1
                final_weekday_position = weekday_calculation(weekday_position)


            elif result_hour <0:
                result_hour +=12
                time='AM'
                day_result=' (' + str(day_number) + ' days later' + ')'
                final_weekday_position = weekday_calculation(weekday_position)


            elif result_hour in range(24,36):
                if result_hour ==24:
                    result_hour -=12
                    time='PM'
                    day_result=' (' + str(day_number+1) + ' days later' + ')'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)

                elif result_hour >24:
                    result_hour -=24
                    time='PM'
                    day_result=' (' + str(day_number+1) + ' days later' + ')'
                    weekday_position +=1
                    final_weekday_position = weekday_calculation(weekday_position)

                else:
                    pass

    #return final weekday_result
    weekday_result = weekday_list[final_weekday_position]

    if weekday == False:
        new_time = str(result_hour) + ':' + result_minute + " " + time + '' + day_result

    else:
        new_time = str(result_hour) + ':' + result_minute + " " + time + ', ' + weekday_result + '' + day_result
    
    #return final result
    return new_time



print(add_time("8:16 PM", "472:02", "tuesday"))
            