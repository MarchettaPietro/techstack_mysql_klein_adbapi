import collections

from event_handler.shared import request_object as req


class EventListRequestObject(req.ValidRequestObject):

    def __init__(self, filters=None):
        if not filters:
            self.filters = {}
        else:
            self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = req.InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return EventListRequestObject(filters=adict.get('filters', None))


class EventShiftRequestObject(req.ValidRequestObject):

    def __init__(self, event_id, secs):
        self.event_id = event_id
        self.secs = secs

    @classmethod
    def from_dict(cls, adict):
        invalid_req = req.InvalidRequestObject()

        if False in [
            'event_id' in adict,
            'secs' in adict,
            adict["event_id"] > 0,
        ]:
            invalid_req.add_error('InputParameters', 'Generic Error')

        if invalid_req.has_errors():
            return invalid_req

        return EventShiftRequestObject(adict["event_id"], adict["secs"])