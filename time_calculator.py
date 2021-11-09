def add_time(start, duration, start_day=None):
    ''' split input to its individual components '''
    start_time, meridiem = start.split()
    start_hour, start_minute = [int(x) for x in start_time.split(":")]
    duration_hour, duration_minute = [int(x) for x in duration.split(":")]
    if(start_day):
        start_day = start_day.capitalize()

    ''' convert 12 hour format to 24 hour format for easier calculations '''
    if(meridiem == "PM"):
        start_hour += 12

    ''' time calculations '''
    start_minute += duration_minute
    start_hour += (start_minute//60)
    start_minute = start_minute % 60
    start_hour += duration_hour
    nextday_counter = start_hour // 24
    start_hour = start_hour % 24

    ''' result formatting '''
    new_time = ''
    new_meridiem = "AM" if start_hour < 11 else "PM"
    if(start_hour > 12):
        start_hour -= 12
    new_time += (str(start_hour) if start_hour != 0 else '12')+":"
    new_time += (str(start_minute if start_minute >
                 9 else "0"+str(start_minute))) + " "
    new_time += new_meridiem
    if(start_day):
        days_of_the_week = ["Sunday", "Monday", "Tuesday",
                            "Wednesday", "Thursday", "Friday", "Saturday"]
        start_day_index = days_of_the_week.index(start_day)
        nextday_of_the_week_index = (start_day_index + nextday_counter) % 7
        new_time += (", " + days_of_the_week[nextday_of_the_week_index])
    if(nextday_counter != 0):
        new_time += " " + (
            f"({nextday_counter} days later)"
            if nextday_counter > 1 else
            "(next day)"
        )

    # print(new_time)
    return new_time


add_time("11:40 AM", "0:25")
