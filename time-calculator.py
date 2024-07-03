def add_time(start_time, duration, start_day=None):
    # Parse start_time
    start_time, period = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if period == 'PM':
        start_hour += 12 if start_hour != 12 else 0

    # Parse duration
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate total minutes
    start_total_minutes = start_hour * 60 + start_minute
    duration_total_minutes = duration_hours * 60 + duration_minutes
    total_minutes = start_total_minutes + duration_total_minutes

    # Calculate new time
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60

    # Determine period (AM or PM)
    if new_hour < 12:
        new_period = 'AM'
        if new_hour == 0:
            new_hour = 12  # Midnight edge case
    else:
        new_period = 'PM'
        if new_hour > 12:
            new_hour -= 12

    # Determine days later
    days_later = total_minutes // 1440

    # Determine day of the week
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if start_day:
        start_day = start_day.capitalize()
        start_index = days_of_week.index(start_day)
        new_day_index = (start_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        if days_later == 1:
            day_string = f", {new_day} (next day)"
        elif days_later > 1:
            day_string = f", {new_day} ({days_later} days later)"
        else:
            day_string = f", {new_day}"
    else:
        if days_later == 1:
            day_string = " (next day)"
        elif days_later > 1:
            day_string = f" ({days_later} days later)"
        else:
            day_string = ""

    # Construct result time string
    new_time = f"{new_hour}:{new_minute:02} {new_period}{day_string}"

    return new_time
