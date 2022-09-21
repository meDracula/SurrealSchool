from collections import namedtuple


class Schedular:
    starting_hour = 9
    schedule = namedtuple('schedule', ['working_hour', 'busses'])

    @property
    def working_hour(self) -> tuple:
        return self.schedule.working_hour

    @working_hour.setter
    def working_hour(self, hours: int):
        self.schedule.working_hour = (starting_hour, starting_hour + hours)

    @property
    def busses(self):
        return self.schedule.busses

    @busses.setter
    def busses(self, hours: int):
        self.schedule.busses = hours
