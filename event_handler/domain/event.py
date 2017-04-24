from datetime import timedelta

from event_handler.shared.domain_model import DomainModel


class Event(object):

    def __init__(self, id, name, active, schedule_time):
        self.id = id
        self.name = name
        self.active = active
        self.schedule_time = schedule_time

    @classmethod
    def from_dict(cls, adict):
        event = Event(
            id=adict['id'],
            name=adict['name'],
            active=adict['active'],
            schedule_time=adict['schedule_time']
        )

        return event

    def postpone(self, by=None):
        if by:
            self.schedule_time += timedelta(seconds=by)

DomainModel.register(Event)

