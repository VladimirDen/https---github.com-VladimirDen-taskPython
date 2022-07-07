class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def __str__(self):
        return str(f"{self.hours}:{self.minutes}:{self.seconds} p.m.(a.m.)")