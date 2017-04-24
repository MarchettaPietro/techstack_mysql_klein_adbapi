from event_handler.shared import use_case as uc
from event_handler.shared import response_object as res
from twisted.internet import defer

class EventListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    @defer.inlineCallbacks
    def process_request(self, request_object):
        domain_events = yield self.repo.list_event(
            event_id=request_object.filters.get('event_id')
        )
        defer.returnValue(res.ResponseSuccess(domain_events))


class EventShiftUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    @defer.inlineCallbacks
    def process_request(self, request_object):
        events = yield self.repo.list_event(
            event_id=request_object.event_id
        )
        if events:
            event = events[0]
            event.postpone(request_object.secs)
            self.repo.save_event(event)
        defer.returnValue(res.ResponseSuccess())
