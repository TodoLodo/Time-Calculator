def add_time(start: str, duration: str, optional=None):
    day = ["Monday", "Tuesday", "Wednesday",
           "Thursday", "Friday", "Saturday", "Sunday"]
    days = 0

    iHours, iMins = tuple(int(n) for n in start[:-3].split(":"))

    iHours += 12 if start.lower().endswith("pm") else 0

    addHours, addMins = tuple(int(n) for n in duration.split(":"))

    iMins += addMins
    iHours += addHours + (iMins // 60)
    iMins = iMins % 60
    days += iHours // 24
    iHours = iHours % 24

    return f"""{'12' if (t:=iHours -12 if iHours > 12 else iHours) == 0 else t}:{'0' if len(str(iMins)) == 1 else ''}{iMins} {"AM" if iHours < 12 else "PM"}{f", {day[([s.lower() for s in day].index(optional.lower()) + days) % len(day)]}" if optional else ""}{f" ({'next' if days == 1 else days} day{'s later' if days > 1 else ''})" if days else ""}"""
