def is_working_on_date(schedule, date):
    """
    schedule — WorkSchedule obyekti
    date — datetime.date obyekti
    """
    weekday = date.weekday()  # 0 = Monday, 6 = Sunday
    return [
        schedule.monday,
        schedule.tuesday,
        schedule.wednesday,
        schedule.thursday,
        schedule.friday,
        schedule.saturday,
        schedule.sunday
    ][weekday]


def get_duration_hours(start, end):
    """
    Vaqtlar orasidagi farqni soatlarda qaytaradi (float)
    """
    from datetime import datetime, date

    dt1 = datetime.combine(date.today(), start)
    dt2 = datetime.combine(date.today(), end)
    duration = dt2 - dt1
    return duration.total_seconds() / 3600


def get_color_by_percent(percent):
    if percent == 0:
        return "white"
    elif 1 <= percent <= 33:
        return "green"
    elif 34 <= percent <= 66:
        return "yellow"
    elif 67 <= percent <= 99:
        return "red"
    return "black"
