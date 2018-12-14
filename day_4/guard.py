class Guard:

    def __init__(self):
        self.most_slept_minutes = {}

    def add_day(self, day):
        for minute in day.minutes_sleeping:
            if minute in self.most_slept_minutes:
                self.most_slept_minutes[minute] +=1
            else:
                self.most_slept_minutes[minute] = 1

    def get_most_slept_minute(self):
        most_slept_minute = 0
        most_slept_minute_amount = 0
        for key in self.most_slept_minutes:
            if self.most_slept_minutes[key] > most_slept_minute_amount:
                most_slept_minute = key
                most_slept_minute_amount = self.most_slept_minutes[key]
        return most_slept_minute, most_slept_minute_amount
