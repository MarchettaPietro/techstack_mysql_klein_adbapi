from event_handler.shared import generic_serializer as gc


class EventEncoder(gc.GenericEncoder):
    encoding_info = {
        "id": int,
        "name": str,
        "active": bool,
        "schedule_time": str
    }
    pass
