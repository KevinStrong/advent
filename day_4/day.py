import re


class Day:

    def __init__(self, guard_id):
        # The id of the guard for the day
        self.guard_id = re.match(".*#(\d{2,4})", guard_id).group(1)
        self.total_minutes_slept = 0
        self.minutes_sleeping = []
        self.fell_asleep_at = 0

    def falls_asleep(self, time):
        self.fell_asleep_at = int(re.match(".*\d\d:(\d\d)", time).group(1))

    def wakes_up(self, time):
        woke_up_at = int(re.match(".*\d\d:(\d\d)", time).group(1))
        self.total_minutes_slept += (woke_up_at - self.fell_asleep_at)
        for i in range(self.fell_asleep_at, woke_up_at):
            self.minutes_sleeping.append(i)

# Example inputs to parse
# '[1518-11-14 23:47] Guard #1291 begins shift', '[1518-06-19 24:14] falls asleep', '[1518-08-28 24:46] wakes up',
