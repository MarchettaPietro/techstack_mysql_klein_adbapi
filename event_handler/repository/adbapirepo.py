from twisted.internet import defer
from event_handler.domain import event


class MysqlAsyncRepo(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @defer.inlineCallbacks
    def list_event(self, event_id=None):
        """
        Retrives all events from mysql db
        Returns domain-level entities
        """
        columns = ["id", "name", "active", "schedule_time"]
        query = "SELECT {} FROM event".format(",".join(columns))
        if event_id:
            query +=" WHERE id={}".format(event_id)
        rows = yield self.dbpool.runQuery(query)
        rows_as_dict = [dict(zip(columns, row)) for row in rows]
        defer.returnValue([event.Event.from_dict(r) for r in rows_as_dict])

    def _save_event(self, txn, event):
        """
        Called within runInteraction this will
        always commit
        """
        query = """
            UPDATE event
            SET name='{}',
                active={},
                schedule_time='{}'
            WHERE id={}
        """.format(
            event.name,
            event.active,
            event.schedule_time,
            event.id
        )
        txn.execute(query)

    @defer.inlineCallbacks
    def save_event(self, event):
        """
        """
        rows = yield self.dbpool.runInteraction(self._save_event, event)
        defer.returnValue(True)
